def make_reverse(word):
    return word[::-1]


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


def is_palindrome(word):
    if word == "":
        return False
    word = word.lower().replace(" ", "")
    return word == word[::-1]
