import networkx as nx

def create_graph():

    graph = nx.Graph()

    graph.add_edge("A","B")

    graph.add_edge("B","C")

    graph.add_edge("C","D")

    return graph
