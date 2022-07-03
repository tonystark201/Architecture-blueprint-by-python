from pathlib import Path

from diagrams import Diagram, Cluster, Edge, Node
from diagrams.aws.compute import Lambda, ECS
from diagrams.aws.database import Dynamodb, RDS, Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.mobile import APIGateway
from diagrams.aws.network import Route53, ALB


class ALBExample:


    def __init__(self):
        self.graph_attr = {
            "layout": "dot",
            "compound": "true", # make edge can link cluster border
            "center": "true"
        }
        self.path = Path(__file__).parent.parent.joinpath("assets")

    def example1(self):
        """
        Serverless with ApiGateway,SQS,Lambda function
        :return:
        """
        with Diagram(
            name="ECS",
            filename=self.path.joinpath('ecs1').as_posix(),
            show=False,
            direction='TB',
            graph_attr=self.graph_attr
        ):

            dns = Route53("DNS")

            with Cluster('Region1'):
                alb1 = ALB('alb')
                dynamo = Dynamodb('Database')

                with Cluster("Private Subnet1"):
                    ecs1 = [ECS("Instance1"),ECS("Instance2"),ECS("Instance3")]

                with Cluster("Private Subnet2"):
                    ecs2 = [ECS("Instance1"), ECS("Instance2"), ECS("Instance3")]

                alb1 >> Edge(lhead="cluster_Private Subnet1")>>ecs1
                alb1 >> Edge(lhead="cluster_Private Subnet2")>>ecs2

                ecs1 >> Edge(label="store data", color="darkblue") >> dynamo
                ecs2 >> Edge(label="store data", color="darkblue") >> dynamo

            with Cluster('Region2'):
                alb2 = ALB('alb')
                dynamo = Dynamodb('Database')

                with Cluster("Private Subnet1"):
                    ecs1 = [ECS("Instance1"), ECS("Instance2"), ECS("Instance3")]

                with Cluster("Private Subnet2"):
                    ecs2 = [ECS("Instance1"), ECS("Instance2"), ECS("Instance3")]

                alb2 >> Edge(lhead="cluster_Private Subnet1") >> ecs1
                alb2 >> Edge(lhead="cluster_Private Subnet2") >> ecs2

                ecs1 >> Edge(label="store data", color="darkblue") >> dynamo
                ecs2 >> Edge(label="store data", color="darkblue") >> dynamo

            dns >> Edge(label="Active(health check)", color="darkgreen") >> alb1
            dns >> Edge(label="Active(health check)", color="darkred") >> alb2


if __name__ == '__main__':
    demo = ALBExample()
    demo.example1()