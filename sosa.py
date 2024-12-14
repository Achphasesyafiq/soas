import networkx as nx
import matplotlib.pyplot as plt

# 1. Group Members
print("""
Our team consists of passionate individuals with expertise in technology, data science, 
and graph theory. Each member brings unique skills in programming, analysis, and visualization 
to help solve complex problems and present data in an understandable way.
""")

# 2. Visualization of Directed and Undirected Graphs

# Create a directed graph
directed_graph = nx.DiGraph()
directed_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4)])

# Visualize the directed graph
plt.figure(figsize=(8, 6))
nx.draw(
    directed_graph,
    with_labels=True,
    node_color='skyblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrowsize=20
)
plt.title("Directed Graph")
plt.show()

# Create an undirected graph
undirected_graph = nx.Graph()
undirected_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4)])

# Visualize the undirected graph
plt.figure(figsize=(8, 6))
nx.draw(
    undirected_graph,
    with_labels=True,
    node_color='lightgreen',
    node_size=2000,
    font_size=12,
    font_weight='bold'
)
plt.title("Undirected Graph")
plt.show()

# 3. Graph Showing Connections Among Cities in Central Java

# Create a graph for cities
cities_graph = nx.Graph()
cities_graph.add_edges_from([
    ("Semarang", "Solo"),
    ("Semarang", "Yogyakarta"),
    ("Solo", "Surakarta"),
    ("Yogyakarta", "Magelang"),
    ("Magelang", "Semarang"),
    ("Solo", "Klaten"),
    ("Surakarta", "Klaten")
])

# Visualize the cities graph
plt.figure(figsize=(10, 8))
nx.draw(
    cities_graph,
    with_labels=True,
    node_color='lightblue',
    node_size=3000,
    font_size=12,
    font_weight='bold',
    edge_color='orange'
)
plt.title("City Connections in Central Java")
plt.show()
