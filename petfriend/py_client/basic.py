import requests

endpoint = "http://localhost:8000/api/"

if __name__ == "__main__":

    response = requests.get(endpoint, params={"abc": 1234}, json={"echo": "Hello from the other side"})
    print(response.status_code)
    print(response.json())
