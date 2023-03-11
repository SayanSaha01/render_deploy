import requests
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://ubaformapi.vercel.app"


def get_access_token(data):
    
    url = BASE_URL + '/auth/login'
    headers = {
        "accept": "application/json",
    }
    response = requests.post(url, params=data, headers=headers)
    
    access_token = response.json()['access_token']
    return access_token






