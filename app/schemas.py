from typing import List

from pydantic import BaseModel


class BaseCorpus(BaseModel):
    id: str
    title: str

    class Config:
        schema_extra = {
            "example": {
                "id": "brown",
                "title": "Brown Corpus"
            }
        }


class ExtendedCorpus(BaseCorpus):
    sents_count: int
    words_count: int

    class Config:
        schema_extra = {
            "example": {
                "id": "brown",
                "sents_count": 57340,
                "title": "Brown Corpus",
                "words_count": 1161192
            }
        }


class Corpora(BaseModel):
    data: List[BaseCorpus]

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "id": "brown",
                        "title": "Brown Corpus"
                    },
                    {
                        "id": "shakespeare",
                        "title": "Shakespeare XML Corpus Sample"
                    }
                ]
            }
        }
