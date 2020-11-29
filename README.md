# Kubernetes Quickly

Code samples and experiments to accompany the book
[Kubernetes Quickly](https://www.manning.com/books/kubernetes-quickly),
by William Denniss.

*This is not an officially supported Google product*

## How to Use This Repository

The folder names (01, 02, etc) correspond to the chapters in the book. There's a subfolder for each
subsection, so samples for Section 5.1.3 in Chapter 5 are found in folder `05/5_1_3`.

All the code listings in the book are included as files in this repo. The intent is to make it
easy to grab the files and try them out yourself, following along with the text of the book.

When a section has multiple discrete samples that should be run independently, they are arranged
into folders and ordered alphabetically, like `A_concept`, `B_concept`

In some cases I've included a more comprehensive sample or experiment in this repo than what's in
the book, in order for you to easily try the concept out yourself. In those cases, the folder
has a `README.md` file with some instructions not found in the book (but still related to
the concept being discussed in that section).

## Running the Samples

All samples assume you have a Kubernetes cluster setup, and `kubectl` authenticated.

Generally, to deploy a sample, from the folder containing the YAML files, 
run `kubectl create -f .` (which will create all the Kubernetes resources defined in the current
folder), and to cleanup, run `kubectl delete -f .`.

The samples are only designed to be deployed one at a time. If you try to deploy 2 without
cleaning up, there will likely be issues.

To reset your cluster to a blank state (CAUTION: only do this
on a test cluster!), you can run the following one-liner:

```
# Delete all objects from the current namespace
kubectl delete service,deployment,ingress,PriorityClass --all
```

