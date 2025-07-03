from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_transcription_english():
    response = client.post("/phonetics/transcription", json={"word": "hello", "language": "en"})
    assert response.status_code == 200
    data = response.json()
    assert data["word"] == "hello"
    assert data["language"] == "en"
    assert isinstance(data["ipa_transcription"], str)
    assert len(data["ipa_transcription"]) > 0

def test_transcription_spanish():
    response = client.post("/phonetics/transcription", json={"word": "hola", "language": "es"})
    assert response.status_code == 200
    data = response.json()
    assert data["word"] == "hola"
    assert data["language"] == "es"
    assert isinstance(data["ipa_transcription"], str)
    assert len(data["ipa_transcription"]) > 0
