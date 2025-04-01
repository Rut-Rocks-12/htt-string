#Using SPARQL and Python to query data from the SPRING database, to visualize protein-protein interactions in order to gain deeper understanding into Huntington’s Disease

Make sure you have all the python packages from the requirements.txt file installed before running any of the python code!

****getting-htt-interactions.py
**
In the getting-htt-interactions.py file, you will first find the code to access the STRING Database's Open API. The STRING-API URL is parsed first, and then a function is defined which takes input for what protein to look for. Within the function certain parameters are defined (such as looking for only human species), and then the API request is sent in the function. Next the function is called, with specifically looking for the htt_protein. From the database, we get RDF data, so together, we save this as a file with all the relevant interactions as a new .rdf file. This file can later be used to create graphs.


