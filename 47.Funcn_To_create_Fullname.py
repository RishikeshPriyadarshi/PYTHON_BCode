from operator import concat
from typing import Concatenate


def create_name(first,last):

    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last #Concatenated the 2-strings

full_name = create_name("the", "king") #Here we returned the value as single string

print(full_name)
    