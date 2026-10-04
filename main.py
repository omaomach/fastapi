from fastapi import FastAPI # import the FastAPI class from the fastapi package
from routers import blog_get
from routers import blog_post

app = FastAPI() # used to create an instance for our application i.e to start the server and provide our paths.
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {
        'message': 'Hello World'
    }
    

# Tags - They allow us to structure and organize our operations within a single file.
# We are able to categorize our operations based on the string we provide in the tags.
