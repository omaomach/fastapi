from typing import Optional
from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id':id,
        'data': blog,
        'version': version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, 
        comment_id: int = Query(None, 
            title='Id of the comment', 
            description='This API simulates posting to a blog',
            alias='commentId',
            deprecated=True
        )
    ):
    return {
        'id': id,
        'blog': blog,
        'comment_id': comment_id
    }
