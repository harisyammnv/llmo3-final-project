import requests
import pandas as pd
from pathlib import Path


def get_jobs_from_linkedin():

    job_per_page_list = []

    pages = 10
    fields = ["LLM Engineer", "NLP Engineer"]
    # "AI Engineer", "Data Scientist", "Gen AI", "Prompt Engineer",


    # Define the URL and parameters
    url = "https://api.scrapingdog.com/linkedinjobs/"

    for field in fields:
        for page in range(1, pages+1):
            params = {
                "api_key": "658306ec7bfa12229a21f004",
                "field": f"{field}",
                "geoid": "103644278",
                "page": f"{page}"
            }

            # Send a GET request with the parameters
            response = requests.get(url, params=params)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Access the response content
                data = response.json()
                data = pd.DataFrame(data)
                job_per_page_list.append(data)

            else:
                print("Request failed with status code:", response.status_code)
        jobs_list = pd.concat(job_per_page_list)
        jobs_list.to_csv(f"Linkedin-Jobs-{field}.csv", index=False)

    # jobs_list = pd.concat(job_per_page_list)
    # jobs_list.to_csv(f"Linkedin-Jobs.csv", index=False)


def postprocess_job_list(data_dir: Path):
    data = []
    for file in data_dir.iterdir():
        df = pd.read_csv(file)
        data.append(df)
    
    data = pd.concat(data)

    data.drop_duplicates(subset=["job_id"], inplace=True)

    data.to_csv(data_dir.joinpath("final-job-list.csv"), index=False)


def extract_job_descriptions(job_list: pd.DataFrame):
    data = []
    for jid in job_list["job_id"]:
        url = "https://api.scrapingdog.com/linkedinjobs"
        api_key = "658306ec7bfa12229a21f004"

        params = {
            "api_key": api_key,
            "job_id": jid
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data.append(pd.DataFrame(response.json()))
        else:
            print(f"Request failed with status code: {response.status_code}")
    data = pd.concat(data)
    data.to_csv("jd-descriptions.csv")

# get_jobs_from_linkedin()
# postprocess_job_list(data_dir=Path.cwd().joinpath("data"))
job_list = pd.read_csv(Path.cwd().joinpath("data", "final-job-list.csv"))
extract_job_descriptions(job_list)

