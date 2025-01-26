"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    new_word ='un' + word
    return(new_word)
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """




def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    suffixes = vocab_words[1:]
    new_words = ' :: '.join([prefix] + [prefix + suffix for suffix in suffixes])
    return new_words

    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """


def remove_suffix_ness(word):
    if word[-4:] == 'ness':
        result = word[:-4]
        if result[-1] == 'i':
            new_word = result[:-1] + 'y'
            return new_word
        return result
    return word


    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """


def adjective_to_verb(sentence, index):
    if sentence[index] == '.':
        new_sentence = sentence.replace('.','')
        my_list = new_sentence.split()
        return my_list[index] + 'en'
        
    else:
        my_list = sentence.split()
        return my_list[index] + 'en'
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    pass
