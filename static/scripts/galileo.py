from requests import post, put, get

product_id = 19481
url = "https://sandbox.galileo-ft.com/instant/v1"

json = {"username": "daj9XXKwNrtn",
        "password": "avNImbDraRPAEjUyHaaz"}

response = post(f'{url}/login', data=json)

resp = response.json()
jwt = resp["access_token"]

headers = {"Authorization": "Bearer {jwt}".format(jwt=jwt)}

aggrements = [12017, 12018, 12019]

mfa_id = 9592
def create_card_holder():
    data = {
        "cardholder": {
            "address": {
                "city": "Salt Lake City",
                "state": "UT",
                "street": "123 Red Street",
                "zip_code": "84121"
            },
            "agreements": aggrements,
            "email": "krapilyadav@gmail.com",
            "first_name": "John",
            "identification": {
                "date_of_birth": "2000-01-01",
                "id": "123456789",
                "id_type": "ssn"
            },
            "income": {
                "amount": "u100k",
                "frequency": "biweekly",
                "occupation": "information_technology",
                "source": "employment"
            },
            "last_name": "Doe",
            "mobile": "1234575890"
        },
        "product_id": product_id
    }
    response = post(f'{url}/cardholders', json=data, headers=headers)
    cardholder_id = response.json()['cardholder_id']


    return cardholder_id

def get_account_info(cardholder_id):

    response = get(f'{url}/cardholders/{cardholder_id}/accounts', headers=headers)


    return response.json()['accounts'][0]


# get balance
#
def transfer_fund(destination_id, amount):
    data = {
        "amount": amount,
        "destination_account_id": destination_id,
        "source_account_id": mfa_id,
    }

    return post(f'{url}/transfers', json=data, headers=headers)

