import requests
import json
from rdflib import Graph, Namespace, URIRef

# Define STRING API URL
STRING_API_URL = "https://string-db.org/api/json/network"

# Define the Huntington's Disease protein (HTT)
htt_protein = "HTT"  # Huntington's disease main protein

# Fetch interactions from STRING API
def fetch_string_interactions(protein):
    params = {
        "identifiers": protein,
        "species": 9606  # Human
    }
    response = requests.get(STRING_API_URL, params=params)

    #Check if API response is valid
    if response.status_code != 200:
        print(f"Error: STRING API failed for {protein}")
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        return []

    try:
        return response.json()
    except json.JSONDecodeError:
        print(f"Error: STRING API returned invalid JSON for {protein}")
        print(f"Response Content: {response.text}")
        return []

# Fetch interactions for HTT
data = fetch_string_interactions(htt_protein)

# Convert STRING interactions to RDF
g = Graph()
STRING = Namespace("http://string-db.org/resource/")
for interaction in data:
    p1 = URIRef(STRING + interaction['preferredName_A'])
    p2 = URIRef(STRING + interaction['preferredName_B'])
    g.add((p1, STRING.interacts_with, p2))

# Save RDF
g.serialize("huntington_string.rdf", format="turtle")
print("RDF file generated: huntington_string.rdf")
