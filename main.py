from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/Welcome")
def read_root():
    return {"HEllo": "Welcome"}


app.mount("/", StaticFiles(directory="public", html = True), name="static")
