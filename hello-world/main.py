from typing import Optional
from fastapi import FastAPI, status, Response # import the FastAPI class from the fastapi package
from enum import Enum

app = FastAPI() # used to create an instance for our application i.e to start the server and provide our paths.

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
@app.get('/blog/all', tags=['blog'], summary='Retrieve all blogs', description='This api call simulates fetching all blogs', response_description='The list of available blogs')
def get_all_blogs(page = 1, page_size: Optional[int] = 10):
    return {
        'message': f"All {page_size} blogs on page {page}"
    }

# Query and Path Parameters
@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid:bool = True, username: Optional[str] = None): # Any function parameters that are not part of the path are called query parameters
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {
        'message': f"The blog type is {type.value}"
    }

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response): # fastAPI used Pydantic to provide parameter/type validation
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f"Blog with id {id}"}
    

# Tags - They allow us to structure and organize our operations within a single file.
# We are able to categorize our operations based on the string we provide in the tags.
