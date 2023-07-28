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


# Q2. Find the pair of numbers whose sum is equal to the given number

list1 = [i for i in range(1,21)]

def Find_Pair(list,sum):
    '''
    input : a list, and a sum of number
    output : a pair of number equals to the sum of number
    '''
    pair=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j] == sum :
                print(list[i],list[j])
                
                    
            
Find_Pair(list1,8)
