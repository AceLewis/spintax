# spintax
A module for parsing spintax, unlike any other modules this also allows the user to escape the special characters used in its syntax.

# How to Install

Install by downloading the [zipped folder](/../../archive/master.zip) or cloning the repository and running:

    python setup.py install
    
# What is spintax
Spintax (also known as spin syntax) is a way to generate strings that are unique but have the same or similar meaning. This can be used in chat bots to reply with pre-created responses and not have the responses all be the same.

There are examples of spintax in use in the examples folder

# The syntax
Spintax aims to replace text within braces (also known as curly brackets) {}; the text that the braces are replaced with is chosen from within the brace.
Within the braces the text that can be chosen is separated by a pipe |.

#####Simple example:

    "{Hey|Hello|Hi} this is {spin syntax|spintax}{.|!|}"

#####Can produce:
* Hey this is spintax.
* Hi this is spin syntax
* Hello this is spintax
* Hi this is spintax!

Unlike other modules, you can escape the special character used in spintax by placing an odd number of "\"'s before the character.

#####Example:

    r"""{Hey|Hello|Hi}{,|} this is {spin syntax|spintax}{.|!|}
    To use spintax enclose \{your|words\} in those brackets and use {a \||the \||a pipe \|} to separate them
    """
    
#####Can produce:
    
 - Hi this is spintax!
   
   To use spintax enclose {your|words} in those brackets and use the |
   to separate them
   
 - Hi, this is spin syntax
   
   To use spintax enclose {your|words} in those brackets and use a | to separate them
   

 - Hello this is spintax. 
   
   To use spintax enclose {your|words} in those
   brackets and use a pipe | to separate them
 
# How to use this module
 
This module can be used to parse spin syntax multiple times and will by default return a list with the a specified number of requested strings.
 
### Parse Function:

#####inputs:

* string: The sting to parse, make sure it is a literal string if you use \ within the string.
* just_string: (Optional) will return the strings separated by a new line if True (Default False).
* number_of_spins: (Optional) the number of times the string will be spun (Default = 1).
* seed: (Optional) if a seed for the random function is desired a seed can be set (Default no seed).

To parse the example string of "{Hey|Hello|Hi} this is {spin syntax|spintax}{.|!|}" 3 times with the random seed of 5 you would do:
 
    import spintax
    spintax.parse(r"{Hey|Hello|Hi} this is {spin syntax|spintax}{.|!|}",number_of_spins=3,seed=5)
    
# Regex help

I would like to say that http://regex101.com helped me a lot with the creation of the Regex, if you need to make Regex I recommend using this website as it is a great tool. They also have an IRC channel that is friendly, and the user OnlineCop helped me with the non capturing group I used to match the spintax brackets.
