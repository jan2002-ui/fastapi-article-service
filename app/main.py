from fastapi import FastAPI, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Article
from app.schemas import ArticleSchema, ArticleCreate

app = FastAPI(title="Article Service")


@app.get("/")
async def root():
    return {"message": "API is online"}


@app.get("/articles/search", response_model=list[ArticleSchema])
async def search_articles(
    keyword: str = "",
    db: AsyncSession = Depends(get_db)
):
    query = select(Article).where(Article.title.contains(keyword))
    result = await db.execute(query)
    return result.scalars().all()


@app.post("/articles", status_code=status.HTTP_201_CREATED)
async def create_article(
    article: ArticleCreate,
    db: AsyncSession = Depends(get_db)
):
    db_article = Article(**article.dict())
    db.add(db_article)
    await db.commit()
    await db.refresh(db_article)
    return db_article