from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Article

async def get_article(db: AsyncSession, article_id: int):
    result = await db.execute(
        select(Article).where(Article.id == article_id)
    )
    return result.scalar_one_or_none()

async def delete_article(db: AsyncSession, article: Article):
    await db.delete(article)
    await db.commit()

