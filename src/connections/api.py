from typing import List

from models.BERT_untrained import bert_untrained_model


def solve_model(words: List[str]) -> List[List[str]]:
    return bert_untrained_model(words)
