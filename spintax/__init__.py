"""
This is my first python project, if you find any errors please submit a pull request on GitHub
I have not looked at PEP 8 so please also tell me how I should write as I am almost certainly
not following the recommended standards
"""

import re
import random


def _replace_literals(string):
    """
    Replace the literal characters that are used if the string needs to
    output a {spintax|string} without spinning it or put a \ before a { or }.

    :param string:
    :return string:
    """

    # Removes double \'s only before a |, {,or }.
    string = re.sub(r'\\{2}(?=(?:\\{2})*[|{}])', r'\\', string)
    # Replaces the literal |, {,and }.
    string = re.sub(r'\\{', r'{', string)
    string = re.sub(r'\\}', r'}', string)
    string = re.sub(r'\\\|', r'|', string)
    return string


def _replace_a_bracket(string, number_of_escapes=None, regex_separator=None, regex_bracket=None):
    """
    Go through the string once and replace one bracket of the spintax with
    a word from within the bracket that is separated by a "|".

    :param string:
    :param number_of_escapes:
    :param regex_separator:
    :param regex_bracket:
    :return string:
    """

    # Find the max number of \'s in a block and save it so it does not need to be re-calculated
    if number_of_escapes is None:
        try:
            # find the maximum number of \'s in a block
            number_of_escapes = len(max(re.findall(re.compile(r'\\+'), string), key=len))
        except ValueError:  # If ValueError none were found
            number_of_escapes = 0
        except:
            raise
        # Compile Regex's only once to save time
        # I am not using .format as when I try to the {} in the Regex messes up and % works
        pattern = "|".join(["(?<!\{)(?<=(?<!\\\\)\\\\{%s})(\|)" % x for x in range(0, number_of_escapes+1, 2)])
        regex_separator = re.compile(pattern)
        regex_bracket = re.compile(r'(?<!\\)((?:\\{2})*)\{([^}{}]+)(?<!\\)((?:\\{2})*)\}')
    # Uses the compiled Regex to find one bracket
    one_bracket = re.search(regex_bracket, string)
    try:
        # Find the first { as the regex matches "{word}" and also "\\{word}"
        pre_slashes = one_bracket.group(0).find("{")
        # Gives a list of the words from ones in the bracket it also removes the None types
        # [0::2] is used as the split will contain the "|"'s on the odd numbers
        pre_split_strings = regex_separator.split(one_bracket.group(0)[pre_slashes:][1:-1])
        list_of_strings = [x for x in pre_split_strings if x is not None][0::2]
    except AttributeError:  # AttributeError if no bracket is found
        # Replace all the literals used in the string
        return _replace_literals(string)
    except:
        raise

    # Find a random word from the list to replace the bracket with
    string_to_replace = random.choice(list_of_strings)

    # Replace the bracket with the word and add the appropriate "\"'s before the word
    string = re.sub(regex_bracket, "\\"*pre_slashes+string_to_replace, string, 1)

    # Call the function again until no more brackets are left
    return _replace_a_bracket(
        string,
        number_of_escapes=number_of_escapes,
        regex_separator=regex_separator,
        regex_bracket=regex_bracket
    )


def parse(string, just_string=False, number_of_spins=1, seed=None):
    """
    Function used to parse the spintax string

    :param string:
    :param just_string:
    :param number_of_spins:
    :param seed:
    :return list:
    """

    # If the user has chosen a seed for the random numbers use it
    if seed is not None:
        random.seed(seed)

    return_list = []
    for _ in range(number_of_spins):
        return_list.append(_replace_a_bracket(string))

    # If the user wants a string to be returned do that by joining the strings
    if just_string:
        return "\n".join(return_list)

    # Otherwise return the list
    else:
        return return_list
