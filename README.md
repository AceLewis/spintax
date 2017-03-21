# spintax
A Python module for parsing spintax, unlike any other module this also allows both nested spintax and the ability to escape special characters.

# How to Install

To install using pip run:

    pip install spintax

Alternatively this module can be installed by downloading the [zipped folder](/../../archive/master.zip) or cloning the repository and running:

    python setup.py install

# What is spintax
Spintax (also known as spin syntax) is a way to create random strings that have the same or similar meaning.

Spintax is very useful as it can be used in programs such as chat bots or video game character speach, it allows the dialog to not sound so repetitive and robotic. Spintax also has great applications in voice assistants such as in Amazon's Alexa, you can easily make skills (apps for the Alexa) that respond without saying the exact same thing every time.

There are examples of spintax in use in the examples folder

# The syntax
Spintax replaces braces (also known as curly brackets, {}) containing text with a random predefined string. The random string is defined withing the braces by using a pipe | as a seperator.

##### Simple example:

    "{Hey|Hello|Hi} this is {spin syntax|spintax}{.|!|}"

##### Can produce:
* Hey this is spintax.
* Hi this is spin syntax
* Hello this is spintax
* Hi this is spintax!

Unlike other modules, you can escape the special characters used in spintax by placing an odd number of "\\"'s before the character.

##### Example:

    r"""{Hey|Hello|Hi}{,|} this is {spin syntax|spintax}{.|!|}
    To use {this module|spintax} enclose \{your|words\} in {those brackets|braces} and use {a \||the \||a pipe (\|)} to separate them
    """

##### Can produce:

 - Hi this is spintax!

   To use spintax enclose {your|words} in braces and use the | to separate them

 - Hi, this is spin syntax

   To use this module enclose {your|words} in those brackets and use a | to separate them


 - Hello this is spintax.

   To use spintax enclose {your|words} in those brackets and use a pipe (|) to separate them

##### Example of Nested Spintax:

       "This is nested {{s|S}pintax|spin syntax}"

##### Can produce:

  - This is nested Spintax
  - This is nested spin syntax
  - This is nested spintax


# How to use this module

This module can be used to spin Spintax easily.

``` Python
import spintax
print(spintax.spin("{Simple|Easy} {example|demonstration}"))
```

### The Spin Function:

##### Inputs:

* string: The sting to parse, make sure it is a literal string if you use \'s within the string.
* seed: (Optional) if a seed for the random function is desired a seed can be set (Default no seed).

# Regex help

I would like to say that http://regex101.com helped me a lot with the creation of the Regex, if you need to make Regex I recommend using this website as it is a great tool. They also have an IRC channel that is friendly, and the user OnlineCop helped me with the non capturing group I used to match the spintax brackets.

# Licence

This software is licensed under the GNU General Public License (version 3) as published by the Free Software Foundation this licence http://www.gnu.org/licenses/ . If you would want a different licence please contact me, on twitter [@_AceLewis](https://twitter.com/@_AceLewis) or Reddit [/u/_AceLewis](https://reddit.com/u/_AceLewis).
