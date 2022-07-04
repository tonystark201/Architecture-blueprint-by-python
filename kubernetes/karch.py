from pathlib import Path

from diagrams import Diagram, Cluster, Edge, Node
from diagrams.digitalocean.storage import Volume
from diagrams.k8s.compute import Pod, Job, ReplicaSet, StatefulSet
from diagrams.k8s.controlplane import ControllerManager, Scheduler, APIServer, Kubelet, KubeProxy
from diagrams.k8s.infra import ETCD
from diagrams.k8s.rbac import ClusterRole
from diagrams.k8s.storage import StorageClass


class K8sExample:

    def __init__(self):
        self.graph_attr = {
            "layout": "neato",
            "compound": "true",  # make edge can link cluster border
            "center": "true"
        }
        self.path = Path(__file__).parent.parent.joinpath("assets")

    def example1(self):
        """
        Serverless with ApiGateway,SQS,Lambda function
        :return:
        """
        with Diagram(
            name="K8S",
            filename=self.path.joinpath('k8s1').as_posix(),
            show=False,
        ):
            with Cluster('Control Plane'):
                etcd = ETCD("etcd")
                cm1 = ControllerManager("Cloud ControllerManager")
                cm2 = ControllerManager("ControllerManager")
                scheduler = Scheduler("Scheduler")
                api_server = APIServer("APIServer")

            api_server >> etcd
            api_server >> Edge(style="dashed") >> cm1
            api_server >> Edge(reverse=True) >> scheduler
            api_server >> Edge(reverse=True) >> cm2

            with Cluster('Data Plane'):

                with Cluster('Worker Node 1'):
                    kubelet1 = Kubelet("Kubelet")
                    kubeproxy1 = KubeProxy("KubeProxy ")

                    with Cluster("Container Runtime",):
                        pods1 = [Pod("pod"), Pod("pod"), Pod("pod")]

                    with Cluster("K8s Objects",):
                        objects1 = [
                            Volume("Volume"),
                            Job("Job"),
                            ReplicaSet("ReplicaSet"),
                            StatefulSet("StatefulSet"),
                            ClusterRole("ClusterRole "),
                            StorageClass("StorageClass ")
                        ]

                with Cluster('Worker Node 2', ):
                    kubelet2 = Kubelet("Kubelet")
                    kubeproxy2 = KubeProxy("KubeProxy ")

                    with Cluster("Container Runtime",):
                        pods2 = [Pod("pod"), Pod("pod"), Pod("pod")]

                    with Cluster("K8s Objects",):
                        objects2 = [
                            Volume("Volume"),
                            Job("Job"),
                            ReplicaSet("ReplicaSet"),
                            StatefulSet("StatefulSet"),
                            ClusterRole("ClusterRole "),
                            StorageClass("StorageClass ")
                        ]

            api_server >> kubelet1 >> Edge(
                htail="cluster_Container Runtime") >> pods1[0]
            api_server >> kubeproxy1

            api_server >> kubelet2 >> Edge(
                htail="cluster_Container Runtime") >> pods2[0]
            api_server >> kubeproxy2

            kubeproxy1 >> Edge(style="dashed", reverse=True) >> kubeproxy2
            Node("User") >> api_server


if __name__ == '__main__':
    k8s = K8sExample()
    k8s.example1()
