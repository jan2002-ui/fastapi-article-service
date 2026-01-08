import httpx

BASE_API = "https://jsonplaceholder.typicode.com/posts"

async def fetch_article(post_id: int) -> dict:
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"{BASE_API}/{post_id}")
        response.raise_for_status()
        return response.json()
