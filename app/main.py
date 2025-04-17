from fastapi import FastAPI
from . import __version__

app = FastAPI(title="Mi FastAPI", version=__version__)

@app.get("/")
def read_root():
    return {"message": "¡Hola FastAPI!", "version": __version__}
