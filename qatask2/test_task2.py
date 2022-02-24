import pytest
import requests

def test_get_code():
    assert requests.get("https://jsonplaceholder.typicode.com/users").status_code==200

def test_header_ct_exists():
    assert len(requests.get("https://jsonplaceholder.typicode.com/users").headers['Content-Type'])>0
    
def test_header_ct_values():
    assert requests.get("https://jsonplaceholder.typicode.com/users").headers['Content-Type']=='application/json; charset=utf-8'

def test_body_users():
    req = requests.get("https://jsonplaceholder.typicode.com/users").json()
    assert len(req) == 10