**Using SPARQL and Python to query data from the SPRING database, to visualize protein-protein interactions in order to gain deeper understanding into Huntington’s Disease**

Before running any Python code, ensure you have installed all required packages listed in the requirements.txt file.

**getting-htt-interactions.py**
The getting-htt-interactions.py file contains code to access the STRING Database's Open API. First, the STRING-API URL is parsed, and a function is defined to specify the target protein. Within the function, key parameters are set, such as filtering for human proteins only, before sending the API request. The function is then called to retrieve data specifically for the HTT protein. The retrieved RDF data is saved as a .rdf file containing all relevant interactions. This file can later be used for visualization and analysis.

**creating-ppi-network.py**
This script utilizes Matplotlib and the previously generated RDF file to visualize the Protein-Protein Interaction (PPI) network. First, the RDF file is parsed to extract individual interactions. Then, using the NetworkX module in Python, a network graph is constructed to display the interactions between proteins. The graph is saved as a .graphml file. Finally, the visualization is generated using the Matplotlib pyplot library.

**confidence_scores.py**
To retrieve confidence scores from the STRING database, another API request is required. This script defines a fetch function that specifies the necessary parameters and runs the request using the HTT protein as input. The output provides a list of interacting proteins along with their respective confidence scores. It is important to note that the database returns protein identifier codes rather than actual protein names.

**confidence_graph.py**
By combining NetworkX with confidence scores, this script visualizes a weighted protein-protein interaction network. The confidence scores are extracted and plotted against the interactions identified in the .rdf file. Using the NetworkX module, connection lines of varying thicknesses are generated to represent different confidence levels, effectively illustrating the strength of interactions between proteins.
