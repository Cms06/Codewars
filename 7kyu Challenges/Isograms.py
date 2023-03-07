'''
Isograms
DESCRIPTION:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''
def is_isogram(string):
    set_str = set(string.lower())
    
    if string == '': #for empty string,  return True
        return True
    
    if len(string) == len(set_str): #for no repeat of letters
        return True
    
    else:
        return False
