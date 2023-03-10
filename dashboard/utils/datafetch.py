import os
import json
import requests

# from dotenv import load_dotenv
# load_dotenv()

import pandas as pd

from .signin import get_access_token,BASE_URL


def fetch_data_fromdb(village_name):
    url = BASE_URL + "/api/get_data"
    signincred = {
        "AADHAR_NO": os.getenv("AADHAR_NO"),
        "password": os.getenv("PASSWORD"),
        "village_name": os.getenv("VILLAGE_NAME"),
        "role": os.getenv("ROLE")
    }
    params = {"village_name": f"{village_name}"}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_access_token(signincred)}",
        "Content-Type": "application/json",
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()


data = fetch_data_fromdb("Sehore") # ["Aastha", "Sehore", "string"]
data_json = json.dumps(data['data'])
df = pd.DataFrame(data["data"]["fam_info"])



