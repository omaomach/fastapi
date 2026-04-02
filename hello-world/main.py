from fastapi import FastAPI # import the FastAPI class from the fastapi package

app = FastAPI() # create an instance for our application

@app.get('/')
def index():
    return {
        'message': 'Hello World'
    }

@app.get('/blog/all')
def get_all_blogs():
    return {
        'message': 'All blogs provided'
    }

@app.get('/blog/{id}')
def get_blog(id: int): # fastAPI used Pydantic to provide parameter/type validation
    return {
        'message': f"Blog with id {id}"
    }
