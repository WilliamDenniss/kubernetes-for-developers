#! /bin/bash

# Script to delete evicted pods.

# ref: https://github.com/kubernetes/kubernetes/issues/55051#issuecomment-342503382

kubectl get pods --all-namespaces -ojson | jq -r '.items[] | select(.status.reason!=null) | select(.status.reason | contains("Evicted")) | .metadata.name + " " + .metadata.namespace' | xargs -n2 bash -c 'kubectl delete pods $0 --namespace=$1'
