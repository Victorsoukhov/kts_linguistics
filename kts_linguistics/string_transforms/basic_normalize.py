from kts_linguistics.chars import RUSSIAN_ALPHABET, ENGLISH_ALPHABET, DIGITS
from kts_linguistics.string_transforms.abstract_transform import AbstractTransform


class BasicNormalizeTransform(AbstractTransform):
    def __init__(self, leave_russian_chars=True, leave_english_chars=True, leave_digits=True, leave_space=True):
        self.allowed_chars = ''
        if leave_russian_chars:
            self.allowed_chars += RUSSIAN_ALPHABET
        if leave_english_chars:
            self.allowed_chars += ENGLISH_ALPHABET
        if leave_digits:
            self.allowed_chars += DIGITS
        if leave_space:
            self.allowed_chars += ' '

    def transform(self, s: str) -> str:
        s = s.strip()
        s = s.lower()
        s = ''.join(c for c in s if c in self.allowed_chars)
        return s
