import math


def is_prime(n):
    """
    Verify if a number is prime

    Iterates through integers from 2 to square root of n to check divisibility

    Params :
    n (int) Number to test

    Return :
    bool : True if n is prime, False if not
    """
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


def circular_number(n):
    """
    Yield a list of circular permuatation of a number

    Iterate through a number and permutate rotatively the digit of the number

    Params :
    n (int) Number to permutate

    Return : 
    list : List result from the circular permutation
    """
    tab = []
    s = str(n)

    for i in range(len(s)):
        s = s[1:] + s[0]
        tab.append(int(s))
    
    return tab

def is_circular_prime(n):
    """
    Check if all number in circulate rotation are prime
    
    Walk trough all circulate number of the integer and test if there are prime

    Params :
    n (int) : Number to test

    Return : 
    bool : True if all circular number are prime , False otherwise 
    """
    for i in circular_number(n):
        if not is_prime(i):
            return False
    return True

if __name__ == "__main__":
    print(is_circular_prime(197))
    print(is_circular_prime(23))
    print(is_circular_prime(13))
    print(is_circular_prime(89))
    print(is_circular_prime(1193))