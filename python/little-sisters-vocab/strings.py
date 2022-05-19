"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "".join(["un", word])


def make_word_groups(vocab_words: list):
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
    prefix = vocab_words[0]
    vocab_words = [prefix + word if word != prefix else prefix for word in vocab_words]
    return " :: ".join(vocab_words)


def remove_suffix_ness(word: str):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    suffix_ness_word = word.rstrip("ness")
    if suffix_ness_word[-1] == "i":
        suffix_ness_word = suffix_ness_word[:-1] + "y"
    return suffix_ness_word


def adjective_to_verb(sentence: str, index: int):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    word = sentence.split()[index]

    return word.strip(".") + "en"
