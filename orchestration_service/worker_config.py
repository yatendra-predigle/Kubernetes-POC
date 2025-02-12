JOB_SPECS = {
    "processor_1": {
        "apiVersion": "batch/v1",
        "kind": "Job",
        "metadata": {
            "name": "placeholder-name-a"
        },
        "spec": {
            "template": {
                "metadata": {
                    "name": "placeholder-pod-a"
                },
                "spec": {
                    "restartPolicy": "Never",
                    "containers": [
                        {
                            "name": "k8s-poc-processor-1",
                            "image": "k8s-poc-processor-1:latest",
                            "env": [
                                {
                                    "name": "FOO",
                                    "value": "BAR"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    },
    "processor_2": {
        "apiVersion": "batch/v1",
        "kind": "Job",
        "metadata": {
            "name": "placeholder-name-b"
        },
        "spec": {
            "template": {
                "metadata": {
                    "name": "placeholder-pod-b"
                },
                "spec": {
                    "restartPolicy": "Never",
                    "containers": [
                        {
                            "name": "k8s-poc-processor-2",
                            "image": "k8s-poc-processor-2:latest"
                        }
                    ]
                }
            }
        }
    }
}
