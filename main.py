def is_even(number):
    return number % 2 == 0


def get_initials(name):
    words = name.split()
    initials = ""

    for word in words:
        initials += word[0].upper()

    return initials


def find_longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def filter_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for character in text.lower():
        if character in vowels:
            count += 1

    return count


def count_words(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count