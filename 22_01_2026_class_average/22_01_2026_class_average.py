def get_average_grade(scores):
    avg = sum(scores) / len(scores)

    if avg >= 97: return "A+"
    if avg >= 93: return "A"
    if avg >= 90: return "A-"
    if avg >= 87: return "B+"
    if avg >= 83: return "B"
    if avg >= 80: return "B-"
    if avg >= 77: return "C+"
    if avg >= 73: return "C"
    if avg >= 70: return "C-"
    if avg >= 67: return "D+"
    if avg >= 63: return "D"
    if avg >= 60: return "D-"
    return "F"


if __name__ == "__main__":
    print(get_average_grade([92, 91, 90, 94, 89, 93])) # should return "A-".
    print(get_average_grade([84, 89, 85, 100, 91, 88, 79])) # should return "B+".
    print(get_average_grade([63, 69, 65, 66, 71, 64, 65])) # should return "D".
    print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100])) # should return "A+".
    print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60])) # should return "C+".
    print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59])) # should return "F".