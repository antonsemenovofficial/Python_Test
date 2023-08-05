import requests

base_url = "https://x-clients-be.onrender.com"


def test_simple_rq():
    resp = requests.get(base_url+'/company')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200

def test_auth():
    creds = {
    'username' : 'michaelangelo',
    'password' : 'party-dude'
    }
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_create_company():
    company = {
    'name' : 'Python',
    'description' : 'Requests'
    }
    creds = {
    'username' : 'michaelangelo',
    'password' : 'party-dude'
    }

    # autificatiom
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]

    # create company
    my_headers = {}
    my_headers["x-clinet-token"] = token

    resp = requests.post(base_url+'/company', json=company, headers=my_headers)
    assert resp.status_code == 201