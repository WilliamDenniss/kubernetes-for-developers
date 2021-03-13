Ever wanted to be able to run a separate gcloud environment? That's what `google/cloud-sdk` can be used for.

These scripts help you create a gcloud environment you can keep around with your favorite customizations, without
impacting the config on your local machine. Great if you want to have multiple contexts for both gcloud and
kubectl, or if you simply don't want to install anything on your local machine besides docker.

Usage:

```
# create a gcloud container, with this repository mounted at /kubernetes-quickly (run once)
./create.sh

# start and attach to an already created container (run each time you want to use the environment)
./attach.sh 

# Once in the container:
gcloud auth login
# ...
# when you're done:
exit

# From another terminal window, run to get an additional shell in the gcloud container
./spawn.sh

# When you no longer need the container (NB. the container can be re-used, keeping your authentication state -- no need to delete after every use)
./delete.sh
```
