from requests import request


def test_create_address():
    payload = request(
        method="post",
        url="http://localhost:8000/address",
        json={"address1": "string", "city": "string", "state": "jk", "zip": "string"},
    )
    assert payload.status_code == 200
