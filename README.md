# Draw Arch blueprint using Python
## Prepare

+ Install chocolately

  > Introduction: Chocolatey has the largest online registry of Windows packages. Chocolatey packages encapsulate everything required to manage a particular piece of software into one deployment artifact by wrapping installers, executables, zips, and/or scripts into a compiled package file.

  So we use chocolately to  install all the packages we needed in windows. It`s very easy to install what you needed.

  Open PowerShell within Adminstration permission.

  ```shell
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
  ```

  Install successfully if you can see something as below.

  ```shell
  PS C:\Windows\system32> choco --version
  1.1.0
  ```

+ Install graphviz 

  ```shell
  choco install graphviz
  ```

+ Install diagrams

  > Introduction: The Diagrams tool allows us to draw and generate system architecture diagrams using Python code. It was born to provide prototypes for those new system architecture designs without any design tools, and we can describe or visualize existing system architecture diagrams.

  Diagrams now supports the graphics including: AWS, Azure, Kubernetes, Ali Cloud, Oracle,etc.

  ```shell
  pipenv install diagrams
  ```

## Draw Diagrams

The Diagrams library has four main components, namely diagrams, nodes, clusters, edges.

1. The 1st core component of the Diagram library is a diagram

   1. filename: specify the file name
   2. outformat: Specify the image generation format
   3. show: whether to display automatically after running
   4. graph_attr: custom Graphviz attributes
   5. node_attr: custom Node attributes
   6. edge_attr: custom edge attributes

2. The 2nd core component of the Diagram library is the node

   1. Node instance, consists of three parts with `provider`,`resource type` and `name`
   2. Data flow
      1. The connection node has no direction (-)
      2. nodes are connected from left to right (>>)
      3. nodes are joined from right to left (<<)

3. The 3rd core component of the Diagram library is the cluster

   Cluster allows you to group or cluster nodes in an independent group. We can use the cluster to create a cluster context and also connect nodes in the cluster to other nodes outside the cluster.

4. The 4th core component of the Diagram library is the edges

   The Edge object contains three properties: label, color, and style

__Note: Getting started drawing is very simple, the basic essentials are to draw with the sample code as a reference. You can check and view the code in this Repo and start your drawing.__
## Example Show

+ The serverless arch by using Lambda,ApiGateway,DynamoDB,etc
[Serverless](https://github.com/tonystark201/Architecture-blueprint-by-python/blob/main/assets/serverless1.png)
+ The ECS deployment
[ECS deployment](https://github.com/tonystark201/Architecture-blueprint-by-python/blob/main/assets/ecs1.png)
+ The ELKB stack
[ELKB](https://github.com/tonystark201/Architecture-blueprint-by-python/blob/main/assets/elkb1.png)
+ The ML example by using eventbridge,rekogniton,translate,etc.
[ML](https://github.com/tonystark201/Architecture-blueprint-by-python/blob/main/assets/ml1.png)
## Summary

The Python drawing library is more practical, but if you are not familiar with `graphviz`, there will be some unsightly situations in the layout of the architecture diagram. The purpose of this library is to make drawing architecture images the same as writing code, but from the actual effect, for some simple architecture diagrams, it is more convenient to use, but for some complex architectures, the layout of the images is ugly. Therefore, this library has a long way to go if it wants to make a difference.

__*Thanks for reading and if you like this repo, please fork and star.*__

## Reference

+ [How to install chocolatey in Windows](https://chocolatey.org/install)
+ [How to install graphviz in Windows](https://graphviz.org/download/)
+ [Python diagrams guide ](https://diagrams.mingrammer.com/docs/guides/diagram)
+ [Graphviz attributes](https://graphviz.gitlab.io/docs/attrs/compound/)

