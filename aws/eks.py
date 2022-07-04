from pathlib import Path
from diagrams import Diagram, Cluster, Node, Edge
from diagrams.aws.analytics import Glue, Athena
from diagrams.aws.compute import ECR, EKS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAM, SecretsManager
from diagrams.aws.storage import S3
from diagrams.onprem.gitops import Argocd
from diagrams.onprem.vcs import Github


class EKSExample:

    """
    Example1: SQL-Based ETL with Apache Spark on Amazon EKS
    """

    def __init__(self):
        self.graph_attr = {
            "layout": "dot",
            "compound": "true",  # make edge can link cluster border
            "center": "true"
        }
        self.path = Path(__file__).parent.parent.joinpath("assets")

    def example1(self):
        with Diagram(
            name="EKS Example",
            filename=self.path.joinpath('eks1').as_posix(),
            show=False,
            direction="TB"
        ):

            node1 = Node("Data Resource")
            node2 = Node("Use Case")

            with Cluster('Security', direction="TB"):
                ss = [
                    ECR("ECR"), IAM("IAM"),
                    SecretsManager("Secrets Manager"),
                    Cloudwatch("Cloudwatch")
                ]

            with Cluster('Workload on EKS', direction="TB"):
                eks = [EKS("EKS Jupyter notebook"), EKS("EKS job")]

            github = Github("Git Script")
            s3 = S3("AWS S3")

            with Cluster('Orchestration on EKS', direction="TB"):
                argo = Argocd("argo")
                argo >> Node("ThirdParty Plugin")

            with Cluster('Data Lake', direction="TB"):
                s3_in = S3("AWS S3")
                glue = Glue("AWS Glue")
                athena = Athena("AWS Athena")
                athena >> s3_in
                athena >> Edge(label="create") >> glue >> node2

            for s in ss:
                for e in eks:
                    s >> e

            node1 >> eks[0] >> github >> s3 >> argo >> eks[1] >> s3_in


if __name__ == '__main__':
    eks = EKSExample()
    eks.example1()
