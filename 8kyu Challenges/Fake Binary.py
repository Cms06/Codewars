'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string


'''


def fake_bin(x):
    low = '43210'
    new = ''
    for i in x:
        if i in low:
            new += '0'
        else:
            new+= '1'
    return new
