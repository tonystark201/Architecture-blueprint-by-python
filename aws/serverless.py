from pathlib import Path
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb, RDS, Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.mobile import APIGateway
from diagrams.aws.network import Route53


class ALBExample:

    def __init__(self):
        self.graph_attr = {
            "fontcolor": "black",
            "fontsize": 30,
        }
        self.path = Path(__file__).parent.parent.joinpath("assets")

    def example1(self):
        """
        Serverless with ApiGateway,SQS,Lambda function
        :return:
        """
        with Diagram(
            name="Serverless",
            filename=self.path.joinpath('serverless1').as_posix(),
            show=False,
            graph_attr=self.graph_attr
        ):
            dns = Route53("DNS")
            api = APIGateway("api")
            with Cluster("Product Service"):
                lambda1 = Lambda("Lambda")
                lambda1 >> Dynamodb("Product DB")

            with Cluster("Order Service"):
                lambda2 = Lambda("Lambda")
                lambda2 >> Dynamodb("Order DB")

            with Cluster("Invoice Service"):
                lambda3 = Lambda("Lambda")
                lambda3 >> RDS("Invoice DB")

            with Cluster("Analysis Service"):
                lambda4 = Lambda("Lambda")
                lambda4 >> Redshift("Analysis")

            sqs = SQS('message queue')
            lambdax = Lambda("Lambda")

            dns >> Edge(color="blue") >> api
            api >> Edge(color="blue") >> lambdax
            lambdax >> Edge(color="blue") >> sqs

            sqs >> Edge(color="darkgreen") >> lambda1
            sqs >> Edge(color="darkgreen") >> lambda2
            sqs >> Edge(color="darkgreen") >> lambda3
            sqs >> Edge(color="darkgreen") >> lambda4


if __name__ == '__main__':
    demo = ALBExample()
    demo.example1()
