Priority classes can be used without preemption (`preemptionPolicy: Never`) which governs the
scheduling and eviction order

To run this test, try the following:

On a cluster with 3 or less nodes:

```
# Fill the cluster with Pods that have no priority set
kubectl create -f deploy_no_priority.yaml

# Check the status
kubectl get pods

# You should see a bunch of pods with "Pending" since we filled up the nodes.

# Create a high priority class
kubectl create -f priorityclass_with_preemption.yaml

# Create a high priority deployment
kubectl create -f deploy_high_priority.yaml

# Check the status
kubectl get pods
```

Normally, since we filled the nodes up with other Pods, Pods in the second deployment would
sit there pending. But with `preemptionPolicy: PreemptLowerPriority`, Pods from the previous
deployment are evicted to make room.

## Cleanup

```
kubectl delete -f .
```
