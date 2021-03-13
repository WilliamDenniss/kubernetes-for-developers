#!/bin/sh

# Spawn a new shell in the gcloud container (it must be running with attach.sh)
docker start gcloud
docker exec -it gcloud bash
