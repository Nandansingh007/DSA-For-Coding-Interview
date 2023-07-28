# Q1. Missing Number
# Finding Missing Number in a array of [1,..,100]

myList = [i for i in range(1,101)]
def find_missing(array, n=100):
    '''
    input : An array of of number having one missing value, and total number of element
    output: find the integer not in a list
    
    '''
    sum1 = 100*101/2
    sum2 = sum(array)
    
    if sum1==sum2:
        print("All number are present in the array")
    else:
        print("The missing number is = ", sum1-sum2)
        
find_missing(myList)
