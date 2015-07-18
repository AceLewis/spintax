"""
This is my first python project, if you find any errors please submit a push request on GitHub
I have not looked at PEP 8 so please also tell me how I should write as I am almost certainly 
not following the recommended standards

"""

import re
import random

def ReplaceAllLiterals(String):
    """
    Replace the literal characters that are used if the string needs to
    output a {spintax|string} without spinnning it or put a \ before a { or }.
    """
    # Removes double \'s only before a |, {,or }.
    String = re.sub(re.compile(r'\\{2}(?=(?:\\{2})*[|{}])'), r'\\' ,String)
    # Replaces the literal |, {,and }.
    String = re.sub(re.compile(r'\\{'), r'{' ,String)
    String = re.sub(re.compile(r'\\}'), r'}' ,String)
    String = re.sub(re.compile(r'\\\|'), r'|' ,String)
    return String

def ReplaceOneBracket(String,NumberOfBackSlashes=None,RegexSeperator=None,RegexBracket=None):
    """
    Go through the string once and replace one bracket of the spintax with a word from within it.
    """
    # Find the max number of \'s in a block and save it so it does not need to be re-calculated each time
    if NumberOfBackSlashes == None:
        try: 
            # find the maximum number of \'s in a block
            NumberOfBackSlashes = len(max(re.findall(re.compile(r'\\+'), String), key=len)) 
        except ValueError: # If ValueError none were found
            NumberOfBackSlashes = 0
        except:
            raise
        # Compile Regex's only once to save time
        # I am not using the .format as when I try to put the {} into the Regex it messed up and % is easier
        RegexSeperator = re.compile("|".join(["(?<!\{)(?<=(?<!\\\\)\\\\{%s})(\|)" % x for x in range(0,NumberOfBackSlashes+1,2)]))
        RegexBracket = re.compile(r'(?<!\\)((?:\\{2})*)\{([^}{}]+)(?<!\\)((?:\\{2})*)\}')
    # Uses the compiled Regex to find one bracket
    OneBracket = re.search(RegexBracket, String)
    try:
        # Find the first { as the regex matches "{word}" and also "\\{word}" 
        ResultToStrip = OneBracket.group(0).find("{")
        # Gives a list of the words from ones in the braket it also removes the None types
        # [0::2] is used as the split will contain the "|"'s on the odd numbers
        ListOfStrings = [x for x in RegexSeperator.split(OneBracket.group(0)[ResultToStrip:][1:-1]) if x is not None][0::2]
    except AttributeError: # AttributeError if no bracket is found
        # Replace all the literals used in the string
        return ReplaceAllLiterals(String)
    except:
        raise
    # Find a random word from the list to replace the bracket with
    StringToReplace = random.choice(ListOfStrings)
    # Replace the bracket with the word and add the appropriate "\"'s before the word
    String = re.sub(RegexBracket, "\\"*ResultToStrip+StringToReplace ,String ,1)
    # Call the function again until no more brackets are left
    return ReplaceOneBracket(String,NumberOfBackSlashes=NumberOfBackSlashes,RegexSeperator=RegexSeperator,RegexBracket=RegexBracket)

def parse(String,JustString=False,NumberOfSpins=1,Seed=None):
    """
    Function used to parse the spintax string
    """
    # If the user has chosen a seed for the random numbers use it
    if Seed!=None:
        random.seed(Seed)
    ReturnList = []
    for x in range(NumberOfSpins):
        ReturnList.append(ReplaceOneBracket(String))
    # If the user wants a string to be returned do that by joining the strings
    if JustString == True:
        return "\n".join(ReturnList)
    # Otherwise return the list
    else:
        return ReturnList