import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# The address of your Orchestrator in K8s.
ORCHESTRATOR_URL = "http://localhost:30022/create-job"

@app.route("/trigger-job", methods=["POST"])
def trigger_job():
    data = request.get_json(force=True)
    processor = data.get("processor")

    if not processor:
        return jsonify({"error": "Missing 'Processor'"}), 400

    # Build request payload to Orchestrator
    payload = {"processor": processor}

    try:
        r = requests.post(ORCHESTRATOR_URL, json=payload, timeout=5)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify(
            {"error": str(e)}
        ), 500

    # Forward the Orchestrator's response to the client
    return jsonify(
        {
            "message": "Job triggered",
            "orchestrator_response": r.json()
        }
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8021, debug=True)
