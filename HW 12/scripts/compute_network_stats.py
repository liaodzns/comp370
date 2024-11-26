import json
import argparse
import networkx as nx
from operator import itemgetter

def create_graph(network_data):
    G = nx.Graph()
    
    # Add edges with weights
    for char1, connections in network_data.items():
        for char2, weight in connections.items():
            G.add_edge(char1, char2, weight=weight)
    
    return G

def get_top_three(metric_dict):
    return [k for k, v in sorted(metric_dict.items(), key=itemgetter(1), reverse=True)[:3]]

def compute_stats(G):
    # Compute centrality metrics
    degree_cent = nx.degree_centrality(G)
    weighted_degree = {node: sum(weight['weight'] for _, weight in G[node].items()) for node in G.nodes()}
    closeness_cent = nx.closeness_centrality(G)
    betweenness_cent = nx.betweenness_centrality(G)
    
    # Get top 3 for each metric
    stats = {
        "degree": get_top_three(degree_cent),
        "weighted_degree": get_top_three(weighted_degree),
        "closeness": get_top_three(closeness_cent),
        "betweenness": get_top_three(betweenness_cent)
    }
    
    return stats

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Input JSON network file path')
    parser.add_argument('-o', '--output', required=True, help='Output JSON stats file path')
    args = parser.parse_args()
    
    # Read network data
    with open(args.input, 'r') as f:
        network_data = json.load(f)
    
    # Create networkx graph
    G = create_graph(network_data)
    
    # Compute statistics
    stats = compute_stats(G)
    
    # Write to JSON file
    with open(args.output, 'w') as f:
        json.dump(stats, f)

if __name__ == "__main__":
    main()
