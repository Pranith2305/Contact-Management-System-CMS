from fastapi import FastAPI

app = FastAPI()

@app.get('/contacts')
def contacts():
    return {"message": "running succesfully"}