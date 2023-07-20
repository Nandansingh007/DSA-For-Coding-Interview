# Notes: 
    # Recursion is mostly used when we can break the problem into sub problems
    # Recursion is used when the time and space complexity is not the main issue
    # Recursion is mostly used in the tree traversal
    
# 1. Calcualting Factorial Using Recursion


def factorial(n):
    # assert {condition}, {message to the user}
    assert n>=0 and int(n)==n, "The passed number should be positive user only"
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("The Factorial of a number Using a recursion",factorial(4))

# 2. Fibonnacii Using recursion


#Time Complexity: 2^n
def fib(n):
    assert n>=0 and int(n) == n, "The given number should be of the positive interger number"
    #base condition
    if n in [0,1]:
        return n
    
    #recursive conditon
    else:
        return fib(n-1)+fib(n+1)
    
# 3. Sum Of a Digits using Recursive

def Sum_Of_Digit(n):
    sum = 0
    
    if n== 0:
        return n
    else:
        return (n%10)+Sum_Of_Digit(n//10)
        
print("The Sum of Digits Using Recursion",Sum_Of_Digit(9999))

# 4. Calculate power using the Recursion

def Power(base,power):
    if power==0:
        return 1
    else:
        return base*Power(base,power-1)
    
print("The Power of a given number using recursio", Power(9,1))


# 5. Finding GCD of two number Using Recursion

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
    
print("The GCD of given number is",gcd(36,12))

# 6. Converting the Decimal Number to the Binary Number

def Decimal_to_Binary(num):
    if num == 1:
        return 1
    else:
        a = num%2
        
        return str(Decimal_to_Binary (num//2)) + str(a)

print("Decimal To Binary Conversion of given number is",Decimal_to_Binary(20))


        
        
        