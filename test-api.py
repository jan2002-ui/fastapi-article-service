from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    """Test if the API root is online"""
    response = client.get("/")
    assert response.status_code == 200
    assert "API is online" in response.json()["message"]

def test_search_articles():
    """Test if the search functionality returns data"""
    # Using 'sunt' as the keyword based on your successful migration
    response = client.get("/articles/search?keyword=sunt")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if len(response.json()) > 0:
        assert "sunt" in response.json()[0]["title"].lower()

def test_search_no_results():
    """Test search with a keyword that doesn't exist"""
    response = client.get("/articles/search?keyword=xyz123abc")
    assert response.status_code == 200
    assert len(response.json()) == 0