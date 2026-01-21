def to_consonant_case(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    
    for letter in s.lower():
        if letter in vowels:
            result.append(letter)
        elif letter.isalpha():
            result.append(letter.upper())
        elif letter == "-":
            result.append("_")
        else:
            result.append(letter)

    return ''.join(result)