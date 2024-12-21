import requests

BASE_API_URL = 'https://api.api-ninjas.com/v1/animals'
FILE_NAME = "Storage/animals.html"


def call_api(name):
    headers = {'X-Api-Key': 's7LNBmnmKxRcVVABhsUUkw==IYip6yjz9nBzLN9s'}
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    return requests.get(api_url, headers)


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

