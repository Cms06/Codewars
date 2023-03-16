'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
'''

def find_uniq(arr):
    myset = set(arr)
    
    if arr.count(list(myset)[0]) == 1:
        return list(myset)[0]
    else:
        return list(myset)[1]
      
      
'''
MORE Simple solution:
def find_uniq(arr):
    myset = set(arr)
    
    for i in myset:
        if arr.count(i)==1:
            return i
'''
