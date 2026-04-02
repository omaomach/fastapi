from typing import Optional
from fastapi import FastAPI # import the FastAPI class from the fastapi package
from enum import Enum

app = FastAPI() # create an instance for our application

@app.get('/')
def index():
    return {
        'message': 'Hello World'
    }

# @app.get('/blog/all')
# def get_all_blogs():
#     return {
#         'message': 'All blogs provided'
#     }

# Default Values
# @app.get('/blog/all')
# def get_all_blogs(page = 1, page_size = 100): # Query parameters - Any function parameters not part of the path
#     return {
#         'message': f"All {page_size} blogs on page {page}"
#     }

# Optional parameters
@app.get('/blog/all')
def get_all_blogs(page = 1, page_size: Optional[int] = None):
    return {
        'message': f"All {page_size} blogs on page {page}"
    }

# Query and Path Parameters
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid:bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {
        'message': f"The blog type is {type.value}"
    }

@app.get('/blog/{id}')
def get_blog(id: int): # fastAPI used Pydantic to provide parameter/type validation
    return {
        'message': f"Blog with id {id}"
    }
