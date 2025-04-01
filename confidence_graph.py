import requests
import networkx as nx
import matplotlib.pyplot as plt

# STRING API base URL
STRING_API_URL = "https://string-db.org/api"

# Request interaction partners with confidence scores
def get_interaction_scores(protein_id, species=9606):
    request_url = f"{STRING_API_URL}/tsv/network?identifiers={protein_id}&species={species}"
    response = requests.get(request_url)
    
    interactions = []
    if response.ok:
        for line in response.text.strip().split("\n")[1:]:  # Skip header
            data = line.split("\t")
            proteinA, proteinB, score = data[0], data[1], float(data[-1])
            interactions.append((proteinA, proteinB, score))
    else:
        print("Error fetching data:", response.status_code)
    return interactions

# Get interactions for HTT
interactions = get_interaction_scores("HTT")

# Create graph
G = nx.Graph()

# Add nodes and edges with weights
for proteinA, proteinB, score in interactions:
    G.add_edge(proteinA, proteinB, weight=score)

# Draw graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Layout for positioning

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue", edgecolors="black")

# Draw edges with varying thickness based on confidence score
edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[d["weight"] * 5 for (_, _, d) in edges], alpha=0.6)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Show plot
plt.title("HTT Protein Interaction Network (STRING Data)")
plt.axis("off")
plt.show()
