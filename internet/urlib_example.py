import requests

__author__ = "Serg"


def get_habrahabra():
    r = requests.get("http://habrahabra.ru/")
    print(r.status_code)
    print(r.headers)
    print(r.content)


def find_pet_by_tag(tag):
    params = {"tags": tag}
    headers={
        "Accept": "application/json"
    }
    url = "http://petstore.swagger.io/v2/pet/findByTags"
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)

    
if __name__ == "__main__":
    find_pet_by_tag("string")
    # get_habrahabra()
