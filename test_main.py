from main import (
    is_even,
    get_initials,
    find_longest_word,
    filter_even_numbers,
    count_vowels,
    count_words
)


def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True


def test_get_initials():
    assert get_initials("Alex Vasilocostas") == "AV"
    assert get_initials("John Smith") == "JS"
    assert get_initials("mary jane watson") == "MJW"


def test_find_longest_word():
    assert find_longest_word(["cat", "elephant", "dog"]) == "elephant"
    assert find_longest_word(["apple", "banana", "pear"]) == "banana"


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []
    assert filter_even_numbers([2, 8, 10]) == [2, 8, 10]


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Alex") == 2
    assert count_vowels("rhythm") == 0


def test_count_words():
    assert count_words("hello world hello") == {
        "hello": 2,
        "world": 1
    }

    assert count_words("cat dog cat bird dog cat") == {
        "cat": 3,
        "dog": 2,
        "bird": 1
    }