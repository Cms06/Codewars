'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''


import string

def is_pangram(s):
    #create a set for the letters of alphabet that is lowercase
    alphabet = set(string.ascii_lowercase)
    #Convert the sentence to lowercase and remove the non letter element using .isalpha()
    letters = set([letter for letter in s.lower() if letter.isalpha()])
    
    #compare both set
    return letters == alphabet
