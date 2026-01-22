# GET https://api.sampleapis.com/coffee/hot
import sqlite3
from typing import List, Dict
import pytest
import requests

@pytest.fixture
def prepare_for_test():
    print("Preparing for test...")
    yield
    print("Cleaning up after test...")

@pytest.mark.usefixtures("prepare_for_test")
def test_get_coffee_hot():
    url = "https://api.sampleapis.com/coffee/hot"
    response = requests.get(url)
    assert response.status_code == 200, f"Wrong code"
    response_data = response.json()
    assert isinstance(response_data, list), "Response is not a list of dictionaries"
    for element in response_data:
        assert "title" in element, "Missing 'title' key in element"
        assert "description" in element, "Missing 'description' key in element"


class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def post_create_invoice(self,link:str,payload:dict):
        response = requests.post(self.base_url + link,payload)
        if response.status_code !=201:
            raise Exception(f"Invoice not created {response.status_code}")
        return response.json()


class DB:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    def _connect(self):
        sqlite3.connect(self.connection_string)
    def get_invoice_by_name(self,name:str)->List[Dict]:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM invoices WHERE name=?", (name,))
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return result



def test_create_invoice():
    data={"name":"Dawid","amount":1000}
    client = Client("https://api.sampleapis.com")
    client.post_create_invoice("/invoices",data)

    #SQL check

