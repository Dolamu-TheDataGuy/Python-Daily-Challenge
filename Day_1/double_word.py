"""
Create a function that accepts a string
The function should return a string.
with each character in the original string doubled

E.g. Martin -> MMaarrttiinn
"""

def double(word: str) -> str: 
    new_word = ""
    if not isinstance(word, str):
        raise TypeError("Please argument should be a string")
    else:
        for letter in word:
            new_letter = letter*2
            new_word += new_letter
    return new_word


print(double("ego"))
print(double("24"))
