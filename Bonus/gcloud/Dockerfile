# Build our own customized container that includes the gcloud CLI
FROM google/cloud-sdk
RUN apt-get update
# Customize this package list with your favorite utilities
RUN apt-get install -y watch vim kubectx
COPY ../../ /kubernetes-quickly
WORKDIR /kubernetes-quickly
