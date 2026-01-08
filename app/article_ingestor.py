import httpx
from sqlalchemy.connectors import asyncio
async def fetch_external_data():
    url = (
        "https://jsonplaceholder.typicode.com/posts"
    )
    async with httpx.AsyncClient() as client:
        # Broken into two lines to fix E501
        response = await client.get(url)
        return response.json()


async def main():
    data = await fetch_external_data()
    print(f"Fetched {len(data)} items")


if __name__ == "__main__":
    asyncio.run(main())