'''
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


'''

def sort_array(source_array):
    #grab all odd number and sort it in new list
    odd_num = sorted([ i for i in source_array if i%2 != 0])
    
    #create new list for final output
    sorted_res = []
    
    #loop
    for i in source_array:
        #if odd, grab the [0] index and append it to the final list.
        if i%2 !=0:
            sorted_res.append(odd_num.pop(0))
        #if even, grab the current value of i and append it to the final list.
        else:
            sorted_res.append(i)
            
    return sorted_res
