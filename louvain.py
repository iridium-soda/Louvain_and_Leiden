"""
A program to show how louvain works. networksx.greedy_modularity_communities in fact.
"""

import networkx as nx
from loguru import logger
import itertools


def cal_modularity(graph: nx.classes.graph.Graph, comms: list[list]):
    """
    To calculate modularity of the current graph
    comms: A list to store communities
    """

    num_edges = graph.number_of_edges()
    num_nodes = graph.number_of_nodes()
    # A = nx.adjacency_matrix(graph)  # To get adjacency_matrix of the graph
    mod = 0  # Final result
    for comm in comms:
        # Get each pair contains 2 nodes in the comm
        for pair in list(itertools.combinations(comm, 2)):
            if graph.has_edge(*pair):
                mod += 1 - (
                    graph.degree(pair[0]) * graph.degree(pair[1]) / (2 * num_edges)
                )
    return mod / (2 * num_edges)


if __name__ == "__main__":
    # Config loguru
    logger.info("Starting demostration")
    # Using Karate Club Graph with 34 nodes and 78 edges. Edges have no weight.
    graph = nx.karate_club_graph()
    MAX_ITER = 20

    comms = [[node] for node in graph]  # To store communities
    # Stop condition: run MAX_ITER rounds
    for iter_loop in range(MAX_ITER):
        for node in graph.nodes():
            current_mod = cal_modularity(graph, comms)
            graph_temp = (
                graph.copy()
            )  # Just shallow copy; only copy nodes and edges without attributes; but it is enough
