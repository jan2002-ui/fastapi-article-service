# tests/test_articles.py
import pytest

@pytest.mark.anyio
async def test_get_articles(client):  # Must start with 'test_'
    response = await client.get("/articles/search")
    assert response.status_code == 200