from functools import lru_cache
from typing import List, Union

from nltk.downloader import Package
from pydantic import BaseSettings


class Settings(BaseSettings):
    corpora_list: List[str] = ['brown', 'reuters', 'conll2002']
    corpora_packages: List[Union[Package, str, None]] = []


@lru_cache()
def get_settings():
    return Settings()
