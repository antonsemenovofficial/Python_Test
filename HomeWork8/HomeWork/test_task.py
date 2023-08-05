import requests

base_url = "https://x-clients-be.onrender.com"

def test_get_company():
    resp = requests.get(base_url+'/company')
    response_body = resp.json()
    first_company = response_body[0]
    id_company = first_company["id"]
    
    my_company_id = {}
    my_company_id["company"] = id_company

    employee = requests.get(base_url+'/employee?', data=my_company_id)

    first_employee = employee.json()
    name_first_emploee = first_company[0]

    assert name_first_emploee["name"] == "Iban"




