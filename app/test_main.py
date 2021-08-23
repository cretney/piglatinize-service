from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_piglatinize_sentence():
    response = client.get("/piglatinize/?text=Hello,%20my%20name%20is%20Alice.")
    assert response.status_code == 200
    assert response.json() == {"original": "Hello, my name is Alice.",
                               "piglatinized": "Ellohay, myay amenay isay Aliceay."}

def test_piglatinize_word():
    response = client.get("/piglatinize/?text=Hello.")
    assert response.status_code == 200
    assert response.json() == {"original": "Hello.", "piglatinized": "Ellohay."}
        
