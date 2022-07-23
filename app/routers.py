from fastapi import APIRouter

from schemas import Corpora, ExtendedCorpus
from wrapper import NLTKCorpus


wrapper_router = APIRouter(prefix="/corpora", tags=["corpora"])

nltk_corpus = NLTKCorpus()


@wrapper_router.get(
    "",
    description="List of all downloaded corpora.",
    summary="NLTK corpora list",
    response_model=Corpora,
    responses={
        200: {
            "description": "List of all downloaded corpora"
        },
    },
)
async def corpora_collection():
    return {"data": nltk_corpus.collection()}


@wrapper_router.get(
    "/{corpus_id}",
    description="Detailed description of corpus",
    summary="NLTK corpus information",
    response_model=ExtendedCorpus,
    responses={
        200: {
            "description": "Requested corpus detailed information"
        },
    },
)
async def corpus_item(corpus_id: str):
    return nltk_corpus.item(corpus_id)
