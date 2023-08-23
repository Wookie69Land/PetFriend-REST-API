import requests

endpoint = "https://dummyjson.com/products/1"

if __name__ == "__main__":

    response = requests.get(endpoint)
    print(response.json())

