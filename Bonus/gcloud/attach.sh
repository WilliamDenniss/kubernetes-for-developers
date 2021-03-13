#!/bin/sh

# Start and attach to the gcloud container (it must have been created earlier with create.sh)
docker start gcloud
docker attach gcloud

