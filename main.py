from fastapi import FastAPI, Request, HTTPException # import the FastAPI class from the fastapi package
from routers import blog_get
from routers import blog_post
from routers import user
from routers import article
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI() # used to create an instance for our application i.e to start the server and provide our paths.
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {
        'message': 'Hello World'
    }

models.Base.metadata.create_all(engine)

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

# Tags - They allow us to structure and organize our operations within a single file.
# We are able to categorize our operations based on the string we provide in the tags.
