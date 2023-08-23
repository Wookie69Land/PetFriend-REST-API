import requests

test_endpoint = "https://dummyjson.com/products/1"
endpoint = "http://localhost:8000/"

if __name__ == "__main__":

    response = requests.get(endpoint)
    print(response.status_code)
    #print(response.json())

