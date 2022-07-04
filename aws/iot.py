from pathlib import Path
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda, EC2
from diagrams.aws.database import Timestream
from diagrams.aws.iot import FreeRTOS, IotDeviceGateway, IotCore, IotEvents, IotRule
from diagrams.aws.management import Cloudwatch, ManagedServices
from diagrams.aws.mobile import APIGateway, Amplify
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client


class IOTExample:
    """
    example1: Smart Metering for Water Utilities
    """


    def __init__(self):
        self.path = Path(__file__).parent.parent.joinpath("assets")

    def example1(self):
        with Diagram(
            name="IOT Example",
            filename=self.path.joinpath('iot1').as_posix(),
            show=False,
            direction="LR"
        ):
            with Cluster('Devices',direction="LR"):
                c1 = Client("BLE")
                c2 = Client("BLE")

                with Cluster('Meter Box1',direction="LR"):
                    f1=FreeRTOS("FreeRTOS")

                with Cluster('Meter Box2',direction="LR"):
                    f2=FreeRTOS("FreeRTOS")

            gateway = IotDeviceGateway("IotDeviceGateway")
            with Cluster('AWS CLoud',direction="LR"):
                iot_core = IotCore("IotCore")
                iot_rule = IotRule("IotRule")

                with Cluster('Management Service'):
                    l1 = Lambda("Lambda Function")
                    ec2_1 = EC2("EC2")

                with Cluster('Monitor&Alerting'):
                    iot_event = IotEvents("IotEvents")
                    cw = Cloudwatch("Cloudwatch")

                with Cluster('Data Storage'):
                    time_stream = Timestream("Timestream")
                    s3 = S3("S3 Bucket")

                with Cluster('Backend Service'):
                    l2 = Lambda("Lambda Function")
                    ec2_2 = EC2("EC2")

                with Cluster('API&Dashboard'):
                    ms = ManagedServices("Lambda Function")
                    api_gateway = APIGateway("APIGateway")
                    amplify = Amplify("Amplify")

            c1>>f1>>gateway
            c2>>f2>>gateway
            gateway>>iot_core
            l1>>iot_core
            iot_core>>iot_rule
            iot_rule >> time_stream
            iot_rule >> s3<< ec2_2<<l2<<api_gateway
            iot_core>>iot_event>>ec2_1

if __name__ == '__main__':
    iot = IOTExample()
    iot.example1()



