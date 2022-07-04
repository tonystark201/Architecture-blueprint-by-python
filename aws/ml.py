from pathlib import Path
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.analytics import KinesisDataStreams, KinesisDataFirehose, Glue, Athena, Quicksight
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.general import User
from diagrams.aws.integration import Eventbridge, SF
from diagrams.aws.management import CloudwatchEventEventBased
from diagrams.aws.ml import Rekognition, Comprehend, Translate
from diagrams.aws.storage import S3


class MLExample:

    def __init__(self):
        self.graph_attr = {
            "layout": "dot",
            "compound": "true",  # make edge can link cluster border
            "center": "true"
        }
        self.path = Path(__file__).parent.parent.joinpath("assets")


    def example1(self):
        with Diagram(
            name="ML Example",
            filename=self.path.joinpath('ml1').as_posix(),
            show=False,
            graph_attr=self.graph_attr
        ):

            with Cluster('Society Media',direction="TB"):
                lambda1 = Lambda(
                    "Identity data to be processed"
                )
                lambda2 = Lambda(
                    "Retrieve meta and data"
                )
                cw = CloudwatchEventEventBased("Schedule data pull")
                eb = Eventbridge("AWS EventBridge")
                s3=S3("Bucket(Ingestion for JSON files)")
                dynamo = Dynamodb("DynamoDB")

            ks = KinesisDataStreams("Kinesis Data Stream")
            lambda01 = Lambda("Ingestion consumer")

            with Cluster('Step Function workflow',direction="TB"):
               sf1 = SF("Topic modeling")
               sf2 = SF("Text interface")

            s3_outer1 = S3("Bucket(Raw text for topic modeling)")
            cw_outer = CloudwatchEventEventBased("Event Scheduler")

            reko=Rekognition("Rekognition")
            comp1 =Comprehend("Comprehend")
            trans = Translate("Translate")
            comp2 = Comprehend("Comprehend")
            eb_outer = Eventbridge("EventBridge(publish interface events)")
            lambda02 = Lambda("JSON transfrmation")
            kdf = KinesisDataFirehose("KinesisDataFirehose")
            s3_outer2 = S3("Bucket(Interface Data)")
            glue = Glue("AWS Glue")
            a = Athena("AWS Athena")
            q = Quicksight("Quicksight Dashboard")

            cw >> lambda1 >> Edge(label="Data2Process") >> eb >> lambda2
            s3 >> eb
            lambda2 >> dynamo
            lambda2 >> ks >> lambda01
            sf1 >> s3_outer1
            sf2 >> s3_outer1
            cw_outer >> sf1
            lambda01 >> Edge(ltail="cluster_Step Function workflow") >> sf1
            sf1 >> Edge(lhead="cluster_Step Function workflow") >> reko
            sf1 >> Edge(lhead="cluster_Step Function workflow") >> comp1
            sf2 >> Edge(lhead="cluster_Step Function workflow") >> trans
            sf2 >> Edge(lhead="cluster_Step Function workflow") >> comp2
            sf2 >> Edge(lhead="cluster_Step Function workflow") >> eb_outer
            eb_outer>>lambda02>>kdf>>s3_outer2<<glue<<a<<q<<User("User")


if __name__ == '__main__':
    ml = MLExample()
    ml.example1()