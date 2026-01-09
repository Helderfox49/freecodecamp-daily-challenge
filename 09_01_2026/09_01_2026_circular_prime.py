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
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def circular_rotation(n):
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
    bool : True if all rotations of n are prime , False if not 
    """
    if not is_prime(n):
        return False
    return all(is_prime(i) for i in circular_rotation(n))


if __name__ == "__main__":
    test_numbers = [197, 23, 13, 89, 1193]
    for number in test_numbers:
        print(f"{number} => {is_circular_prime(number)}")   