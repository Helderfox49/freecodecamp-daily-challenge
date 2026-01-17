def knight_moves(position):
    col = ord(position[0]) - ord("A")
    row = int(position[1])-1
    count = 0

    if col + 2 <= 7: 
        if row + 1 <= 7:
            count += 1
        if row - 1 >=0:
            count += 1

    if col - 2 >= 0: 
        if row + 1 <= 7:
            count += 1
        if row - 1 >=0:
            count += 1

    if row + 2 <= 7:
        if col + 1 <= 7:
            count += 1
        if col - 1 >=0:
            count +=1

    if row - 2 >= 0: 
        if col + 1 <= 7:
            count += 1
        if col - 1 >=0:
            count +=1
    
    return count


if __name__ == "__main__":
    print(knight_moves("A1")) # should return 2.
    print(knight_moves("D4")) # should return 8.
    print(knight_moves("G6")) # should return 6.
    print(knight_moves("B8")) # should return 3.
    print(knight_moves("H3")) # should return 4