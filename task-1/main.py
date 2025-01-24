#!/usr/bin/env python

import pandas as pd
import networkx as nx

def create_graph(edges):
    """Creating a graph with edges and bandwidths."""
    G = nx.DiGraph()
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    return G

def calculate_max_flow(G, source, sink):
    """Calculating the maximum flow in a graph."""
    return nx.maximum_flow(G, source, sink)

def analyze_terminal_to_store_results(flow_dict, terminals, stores):
    """Analyze the flow from terminals to stores via intermediate nodes."""
    results = []
    for terminal in terminals:
        if terminal in flow_dict:
            for intermediate_node, flow_to_intermediate in flow_dict[terminal].items():
                if intermediate_node in flow_dict:
                    for store, flow_to_store in flow_dict[intermediate_node].items():
                        if store in stores:
                            # Flow from terminal to store via intermediate node
                            flow = min(flow_to_intermediate, flow_to_store)
                            results.append([terminal, store, flow])
    return results

def display_results(results):
    """Displaying results in a table."""    
    df = pd.DataFrame(results, columns=["Terminal", "Store", "Actual Flow (units)"])
    return df

def main():
    edges = [
        ("Terminal 1", "Warehouse 1", 25),
        ("Terminal 1", "Warehouse 2", 20),
        ("Terminal 1", "Warehouse 3", 15),
        ("Terminal 2", "Warehouse 3", 15),
        ("Terminal 2", "Warehouse 4", 30),
        ("Terminal 2", "Warehouse 2", 10),
        ("Warehouse 1", "Store 1", 15),
        ("Warehouse 1", "Store 2", 10),
        ("Warehouse 1", "Store 3", 20),
        ("Warehouse 2", "Store 4", 15),
        ("Warehouse 2", "Store 5", 10),
        ("Warehouse 2", "Store 6", 25),
        ("Warehouse 3", "Store 7", 20),
        ("Warehouse 3", "Store 8", 15),
        ("Warehouse 3", "Store 9", 10),
        ("Warehouse 4", "Store 10", 20),
        ("Warehouse 4", "Store 11", 10),
        ("Warehouse 4", "Store 12", 15),
        ("Warehouse 4", "Store 13", 5),
        ("Warehouse 4", "Store 14", 10),
    ]

    terminals = ["Terminal 1", "Terminal 2"]
    stores = [f"Store {i}" for i in range(1, 15)]

    G = create_graph(edges)
    overall_results = []
    total_flow = 0

    for terminal in terminals:
        for store in stores:
            if nx.has_path(G, terminal, store):  # Ensure a path exists
                flow_value, flow_dict = calculate_max_flow(G, terminal, store)
                total_flow += flow_value
                results = analyze_terminal_to_store_results(flow_dict, [terminal], stores)
                overall_results.extend(results)

    df = display_results(overall_results)
    # Filter rows where "Actual Flow (units)" > 0
    df_filtered = df[df["Actual Flow (units)"] > 0]
    print(df_filtered)
    print(f"Total maximum flow: {total_flow}")

if __name__ == "__main__":
    main()
