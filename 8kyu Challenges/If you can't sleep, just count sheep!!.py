'''
If you can't sleep, just count sheep!!

DESCRIPTION:
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

'''

def count_sheep(n):
    x =""
    if n > 0:
        for i in range(1,n+1):
            x+=f'{i} sheep...'
    else:
        print("")
    return x