from fastapi import FastAPI
from nltk import corpus, download
from uvicorn import run

from config import get_settings
from routers import wrapper_router


# App

app: FastAPI = FastAPI(
    title="nltk-wrapper",
    description="Service over NLTK Corpora module.",
    version="0.1.0",
)

SETTINGS = get_settings()


@app.on_event("startup")
async def startup_event():
    for crp in SETTINGS.corpora_list:
        try:
            getattr(corpus, crp)
            SETTINGS.corpora_packages.append(crp)
        except AttributeError:
            pass
    download(SETTINGS.corpora_packages)

# API

api: FastAPI = FastAPI(
    title="nltk-wrapper-API",
    description="API for nltk-wrapper.",
    version="0.1.0",
)

app.mount("/api", api)
api.include_router(wrapper_router)


if __name__ == "__main__":
    run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
