import requests

def test_get_recursos():
    response = requests.get("http://127.0.0.1:8000/api/recursos/")
    
    assert response.status_code == 200