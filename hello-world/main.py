from fastapi import FastAPI # import the FastAPI class from the fastapi package

app = FastAPI() # create an instance for our application

@app.get('/')
def index():
    return {
        'message': 'Hello World'
    }

@app.get('/blog/{id}')
def getBlog(id: int):
    return {
        'message': f"Blog with id {id}"
    }