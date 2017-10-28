import pymorphy2

from kts_linguistics.corpora.corpora import Corpora
from kts_linguistics.string_transforms.phonetize import phonetize


def normalize_corpora(corpora: Corpora) -> Corpora:
    new_corpora = Corpora()
    morph = pymorphy2.MorphAnalyzer()
    for word, count in corpora.words_with_counts():
        new_corpora.increment_popularity(morph.parse(word)[0].normal_form, count)
    return new_corpora


def phonetize_corpora(corpora: Corpora) -> Corpora:
    new_corpora = Corpora()
    for word, count in corpora.words_with_counts():
        new_corpora.increment_popularity(phonetize(word), count)
    return new_corpora