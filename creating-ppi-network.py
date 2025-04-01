import pandas as pd
from rdflib import Graph
import networkx as nx
import matplotlib.pyplot as plt

# Load RDF file
g = Graph()
g.parse("huntington_string.rdf", format="turtle")

# Extract protein interactions
data = []
for subj, _, obj in g:
    protein1 = subj.split("/")[-1]  # Extract protein names
    protein2 = obj.split("/")[-1]
    data.append((protein1, protein2))

# Create NetworkX graph
G = nx.Graph()
for subj, _, obj in g:
    protein1 = subj.split("/")[-1]
    protein2 = obj.split("/")[-1]
    G.add_edge(protein1, protein2)

# Save as GraphML for Gephi
nx.write_graphml(G, "huntington_string.graphml")

# Draw the network
plt.figure(figsize=(10, 7))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", font_size=10)
plt.show()

  
