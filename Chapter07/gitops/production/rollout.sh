#! /bin/sh

if [ $(../gitops_check.sh; echo $?) != 0 ]; then exit 1; fi

kubectl apply -f .
