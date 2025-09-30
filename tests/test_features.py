import pytest
from app.features import (
    is_palindrome,
    is_anagram,
    make_reverse,
)

@pytest.mark.parametrize(
        'word, expected', [
            ("А роза упала на лапу Азора", True),
            ("Палиндром", False),
            ("", False),
        ]
)
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected

@pytest.mark.parametrize(
    "word1, word2, expected", [
        ('cat', 'act', True),
        ('cat', 'dog', False),
        ('', '', True),
    ]
)
def test_is_anagram(word1, word2, expected):
    assert is_anagram(word1, word2) == expected

@pytest.mark.parametrize(
    "word, expected", [
        ('cat', 'tac'),
        ('dog', 'god'),
        ('', ''),
    ]
)
def test_make_reverse(word, expected):
    assert make_reverse(word) == expected