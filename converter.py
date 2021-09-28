import pandas as pd
import string

ascii = {}

class Converter():
    """Class for multiplying dec from ASCII table by 10 or return 0.
    Args:
        None
    """
    for letter in (string.ascii_uppercase + string.ascii_lowercase):
        ascii[letter] = ord(letter)

def use(list):
    """multiplying ascii dec by 10 or return 0 under certains rules
    @params:
    list: list to specify to convert letter into ASCII dec 
    """
    listToReturn = []
    for letter in list:
        # Some verifications
        if (isinstance(letter,int)): continue
        if not letter: continue
        if letter.isupper(): # Check if it's uppercase to apply the rule for below 'H'
            response = (ascii.get(letter)*10, 0)[ascii.get(letter) >= 72] # I tried to make [letter.isupper() and alist.get(letter) >= 72] but it wouldn't work
        else: # Apply the rule for below 'h'
            response = (ascii.get(letter)*10, 0)[ascii.get(letter) >= 104]
        listToReturn.append(response)
    return pd.DataFrame(listToReturn).to_json(orient='values')