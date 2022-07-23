from typing import Dict, List, Union

from nltk import corpus

from config import get_settings


SETTINGS = get_settings()


class NLTKCorpus:

    def __init__(self) -> None:
        pass

    def collection(self) -> List[Union[Dict[str, str], None]]:
        """
        Get a collection of downloaded corpora.
        """
        return [
            {"id": crp.id,  "title": crp.name}
            for crp in SETTINGS.corpora_packages
        ]

    def item(self, corpus_id: str) -> Dict[str, Union[str, int]]:
        """
        Get detailed info about downloaded corpora.
        """
        result = {"id": corpus_id}

        for crp in SETTINGS.corpora_packages:
            if crp.id == corpus_id:
                result['title']: str = crp.name

        crp_pack = getattr(corpus, corpus_id)
        result['sents_count']: int = len(crp_pack.sents())
        result['words_count']: int = len(crp_pack.words())

        return result
