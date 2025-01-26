"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    lowercase_title = title
    proper_title = lowercase_title.title()
    return proper_title
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """



def check_sentence_ending(sentence):
    sentence_to_check = sentence
    return sentence_to_check.endswith('.')
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """


def clean_up_spacing(sentence):
    sentence_with_space = sentence
    return sentence_with_space.strip()
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """


def replace_word_choice(sentence, old_word, new_word):
    original_sentence = sentence
    new_sentence = sentence.replace(old_word, new_word)
    return new_sentence
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    pass
