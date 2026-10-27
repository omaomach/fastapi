from fastapi import FastAPI, Request, HTTPException # import the FastAPI class from the fastapi package
from routers import blog_get, blog_post, user, article, product
from auth import authentication
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # used to create an instance for our application i.e to start the server and provide our paths.
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)

@app.get('/')
def index():
    return {
        'message': 'Hello World'
    }

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={
            'detail': exc.name
        }
    )
    
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)

# Tags - They allow us to structure and organize our operations within a single file.
# We are able to categorize our operations based on the string we provide in the tags.

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ['*']
)
