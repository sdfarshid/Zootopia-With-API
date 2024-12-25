import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def call_api(name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    return requests.get(api_url, headers={'X-Api-Key': API_KEY})



def process_fetching_data_from_API(animal_name):
    response = call_api(animal_name)
    if response.status_code == requests.codes.ok:
        result_data = response.json()
        if len(result_data) <= 0:
            raise ValueError(f"<h2>The animal {animal_name} doesn't exist.</h2>")
        else:
            return response.text
    else:
        print("Error:", response.status_code, response.text)
        return False

