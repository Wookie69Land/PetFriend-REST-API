import requests

endpoint = "http://localhost:8000/api/"

if __name__ == "__main__":

    # response_get = requests.get(endpoint)
    # print(response_get.status_code)
    # print(response_get.json())

    response_post = requests.post(endpoint, json={'id': 1})
    print(response_post.json())
