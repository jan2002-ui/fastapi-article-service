from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    body: str


class ArticleCreate(ArticleBase):
    pass


class ArticleSchema(ArticleBase):
    id: int

    class Config:
        from_attributes = True  # Two spaces before this comment