import uuid
import copy
from flask import Flask, request, jsonify
from kubernetes import client, config

from worker_config import JOB_SPECS

app = Flask(__name__)

# Load your K8s config
try:
    config.load_incluster_config()   # For running inside the cluster
except:
    config.load_kube_config()        # For local dev (Docker Desktop, etc.)

batch_v1 = client.BatchV1Api()

@app.route("/create-job", methods=["POST"])
def create_job():
    data = request.get_json(force=True)
    processor = data.get("processor")

    if not processor:
        return jsonify({"error": "Missing 'processor'"}), 400

    # Lookup the relevant job manifest in the dictionary
    job_template = JOB_SPECS.get(processor)
    if not job_template:
        return jsonify({"error": f"Unknown processor '{processor}'"}), 400

    job_manifest = copy.deepcopy(job_template)

    # Generate a unique job name
    job_name = f"dynamic-job-{processor.lower()}-{uuid.uuid4().hex[:5]}"

    # Override the metadata.name in the job
    job_manifest["metadata"]["name"] = job_name

    # override the pod template name if desired
    if "template" in job_manifest["spec"]:
        if "metadata" in job_manifest["spec"]["template"]:
            job_manifest["spec"]["template"]["metadata"]["name"] = job_name

    # Create the Job in Kubernetes
    try:
        resp = batch_v1.create_namespaced_job(
            namespace="default",
            body=job_manifest
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "message": f"K8s Job created for worker '{processor}'",
        "job_name": job_name
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8022)
