import requests

endpoint = "http://localhost:8000/api/"

if __name__ == "__main__":

    # response_get = requests.get(endpoint)
    # print(response_get.status_code)
    # print(response_get.json())

    # response_post = requests.post(endpoint, json={'id': 1})
    # print(response_post.json())

    endpoint = endpoint + 'add/'
    pet = {
        'name' : 'Good boy',
        'genre' : 1,
        'species' : 1,
        'user' : 2,
    }
    response_add = requests.post(endpoint, json=pet)
    print(response_add.json())
