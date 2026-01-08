def is_sorted(arr):
    asc = sorted(arr)
    desc = asc[::-1]

    if arr == asc:
        return "Ascending"
    elif arr == desc:
        return "Descending"
    return "Not sorted"