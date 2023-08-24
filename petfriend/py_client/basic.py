import requests

endpoint = "http://localhost:8000/api/"

if __name__ == "__main__":

    response = requests.get(endpoint)
    print(response.status_code)
    print(response.json())

