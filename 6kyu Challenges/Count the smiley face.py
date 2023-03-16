'''
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
'''

def count_smileys(arr):
    count = 0
    eye = ':;'
    nose = '-~'
    mouth = ')D'
    if len(arr)!=0:
        for smiley in arr:
            if len(smiley) == 3:
                if smiley[0] in eye and smiley[1] in nose and  smiley[2] in mouth:
                    count+=1
            elif len(smiley) == 2:
                if smiley[0] in eye and smiley[1] in mouth:
                    count+=1
                    
    else:
        return 0
    
    return count
