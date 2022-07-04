from pathlib import Path

from diagrams import Diagram, Cluster, Edge
from diagrams.elastic.elasticsearch import Logstash, Elasticsearch, Kibana, Beats
from diagrams.onprem.network import Apache, Nginx
from diagrams.programming.language import Python, Go


class ELKBExample:

    def __init__(self):
        self.path = Path(__file__).parent.parent.joinpath("assets")

    def example1(self):
        with Diagram(
            name="ELKB Example",
            filename=self.path.joinpath('elkb1').as_posix(),
            show=False,
            direction="LR"
        ):

            logstash = Logstash("Logstash")
            with Cluster('Elasticsearch Cluster', direction="TB"):
                e1 = Elasticsearch("Elasticsearch Master")
                e2 = Elasticsearch("Elasticsearch Node1")
                e3 = Elasticsearch("Elasticsearch Node2")

                e1 >> Edge(style="dashed", reverse=True) >> e2
                e1 >> Edge(style="dashed", reverse=True) >> e3

            kibana = Kibana("Kibana")

            Apache("Apache") >> Beats("Beats") >> Edge(
                color="darkblue", label="Logs") >> logstash
            Nginx("Nginx") >> Beats("Beats") >> Edge(
                color="darkblue", label="Logs") >> logstash
            Python("Python") >> Beats("Beats") >> Edge(
                color="darkblue", label="Logs") >> logstash
            Go("Go") >> Beats("Beats") >> Edge(
                color="darkblue", label="Logs") >> logstash
            logstash >> Edge(color="darkblue", label="Ingested Logs") >> e1
            e1 << Edge(color="darkblue", label="Search") << kibana


if __name__ == '__main__':
    elkb = ELKBExample()
    elkb.example1()
