import requests

url = "https://api.scrapingdog.com/linkedinjobs"
api_key = "658306ec7bfa12229a21f004"
job_id = "3539667535"

params = {
    "api_key": api_key,
    "job_id": job_id
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code: {response.status_code}")
