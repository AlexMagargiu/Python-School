import networkx as nx
n = int(input("Enter the number of nodes: "))
print("Enter each edge on a new line in the format '0 1'. Type 'done' when finished:")

muchii = []
while True:
    edge_input = input()
    if edge_input.lower() == 'done':
        break
    u, v = map(int, edge_input.split())
    muchii.append((u, v))

graph = nx.DiGraph(muchii)
matrix = nx.adjacency_matrix(graph, list(range(n)))

print("Adjacency matrix of the graph:")
print(matrix.todense())
print('\n')

node = int(input("Enter the node for which you want to check predecessors and successors: "))
predecessors = list(graph.predecessors(node))
successors = list(graph.successors(node))

print(f"Predecessors of node {node}: {predecessors}")
print(f"Successors of node {node}: {successors}")

num_arcs = len(muchii)
print(f"\nNumber of arcs in the graph: {num_arcs}")
