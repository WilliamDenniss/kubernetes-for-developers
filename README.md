# Kubernetes for Developers

Code samples and experiments to accompany the book
[Kubernetes for Developers](https://www.manning.com/books/kubernetes-for-developers),
by William Denniss.

*This is not an officially supported Google product*

<img src="Denniss-Kubernetes-720.png" width="360">

## How to Use This Repository

The folder names (Chapter01, Chapter02, etc) correspond to the chapters in the book. There's a subfolder for each
subsection, so samples for Section 5.1.3 in Chapter 5 are found in folder `Chapter05/5.1.3_DescriptiveTitle`. If
a section has multiple discrete samples, they will be in separate folders like `Chapter05/5.1.3_Sample1`, 
`Chapter05/5.1.3_Sample2`.

All the code listings in the book are included as files in this repo. The intent is to make it
easy to grab the files and try them out yourself, following along with the text of the book.

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

