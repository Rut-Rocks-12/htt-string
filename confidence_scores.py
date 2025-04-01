import requests

# STRING API base URL
STRING_API_URL = "https://string-db.org/api"

# Request interaction partners with confidence scores
def get_interaction_scores(protein_id, species=9606):
    request_url = f"{STRING_API_URL}/tsv/network?identifiers={protein_id}&species={species}"
    response = requests.get(request_url)
    
    if response.ok:
        for line in response.text.strip().split("\n")[1:]:  # Skip header
            data = line.split("\t")
            proteinA, proteinB, score = data[0], data[1], float(data[-1])
            print(f"{proteinA} interacts with {proteinB} → Confidence: {score}")
    else:
        print("Error fetching data:", response.status_code)

# Get HTT (Huntingtin) interaction scores
get_interaction_scores("HTT")
