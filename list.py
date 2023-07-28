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
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j] == sum :
                print(list[i],list[j])
                
            
Find_Pair(list1,8)

# Q3. How to check if a array contain a number

list2 = [i for i in range(1,21)]

def Check_Number(list,n):
    '''
    input : a list and a number to check
    output : whether the number is present or not
    '''
    for i in range(len(list)):
        if n == list[i]:
            print("The number is present in the list: ", n)
            break
        else:
            print("The number is not present in the list")
            break
            
Check_Number(list2, 0)

# Q3. Find the maximum product of two element in the number, if all number is positive

list3 = [10,13,4,5,9,5,22,45,32,13]

def Max_Product(list):
    '''
    Input : list
    Output : The maximum product and the pair that makes the product maximum
    '''
    
    max = 0
    for i in range(len(list3)):
        for j in range(i+1,len(list3)):
           if list[i]*list[j] > max:
               max = list[i]*list[j]
               pair = str(list[i])+ "," +str(list[j])
    print("The maximum product is: ", max, "The pair of maximum product is : ", pair)

Max_Product(list3) 


# Q4. Find the if the list has all the number unique

list4 = [10,13,4,5,9,1,22,45,32,3]

def IsUnique(list):
    '''
    Input : list
    Output : Unique if all the element is unique
    '''
    for i in range(len(list4)):
        for j in range(len(list4)):
            if i!=j:
                if list[i] == list[j]:
                    print("The list is not unique",list[i])
                    break
    print("The list is unique")
    
IsUnique(list4)


# Q5. Finding Permuatation
# Permutation - Same elements but in different order

a = [1,2,3,4,5]
b = [2,3,4,2,5]

def Permutation(a,b):
    '''
    Input : two list
    Output: weather the input list is palindrome
    '''
    a.sort()
    b.sort()
    
    if len(a) != len(b):
        print("Not Permutated")
    else:
        for i in range(len(a)):
            if a[i] == b[i]:
                if a[i] == a[-1]:
                    print("permuted")
                continue
            else:
                print("Not Permutated")
                break
            
Permutation(a,b)


#  Q7. Rotate Matrix

a = [[1,2,3],[4,5,6],[7,8,9]]

        
    
        

