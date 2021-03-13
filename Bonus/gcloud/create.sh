#!/bin/sh

# Build the container image and tag it gcloud_container
docker build -t gcloud_container .

# Create a container named gcloud using the image named gcloud_container, and mount the example files
docker create -it --mount type=bind,source="$(pwd)/../..",target=/kubernetes-quickly --name gcloud gcloud_container bash
