import asyncio
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# Absolute imports - requires app/__init__.py to exist
from app.database import Base, DATABASE_URL
from app.models import Article

load_dotenv()

# Source SQLite path
SQLITE_URL = "sqlite+aiosqlite:///./scrapping.db"


async def run_migration() -> None:
    print("Connecting to databases...")

    sqlite_engine = create_async_engine(SQLITE_URL)
    pg_engine = create_async_engine(DATABASE_URL)

    # 1. DROP and RECREATE tables to ensure columns match your code
    async with pg_engine.begin() as conn:
        print("Refreshing PostgresSQL schema...")
        # WARNING: This deletes the 'articles' table in Postgres before recreating it
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    sqlite_session_factory = async_sessionmaker(sqlite_engine, class_=AsyncSession)
    pg_session_factory = async_sessionmaker(pg_engine, class_=AsyncSession)

    async with sqlite_session_factory() as s_db, pg_session_factory() as p_db:
        # ... rest of your code (the SELECT and INSERT logic) ...
        print("Reading data from SQLite (Title and Body only)...")

        # Using raw SQL to avoid model attribute errors
        result = await s_db.execute(text("SELECT title, body FROM articles"))
        rows = result.fetchall()

        if not rows:
            print("No data found in scrapping.db.")
            return

        print(f"Found {len(rows)} articles. Moving to PostgresSQL...")

        for row in rows:
            # We map row[0] -> title and row[1] -> body
            new_article = Article(
                title=row[0],
                body=row[1]
            )
            p_db.add(new_article)

        await p_db.commit()
        print("--- Migration Successful! ---")

    await sqlite_engine.dispose()
    await pg_engine.dispose()


if __name__ == "__main__":
    try:
        asyncio.run(run_migration())
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")