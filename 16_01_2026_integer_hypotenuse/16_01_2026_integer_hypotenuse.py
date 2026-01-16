def is_integer_hypotenuse(a, b):
    if ((a*a + b*b)**0.5) == int((a*a + b*b)**0.5): 
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    print(is_integer_hypotenuse(3, 4)) # should return True.
    print(is_integer_hypotenuse(2, 3)) # should return False.
    print(is_integer_hypotenuse(5, 12)) # should return True.
    print(is_integer_hypotenuse(10, 10)) # should return False.
    print(is_integer_hypotenuse(780, 1040)) # should return True.
    print(is_integer_hypotenuse(250, 333)) # should return False.