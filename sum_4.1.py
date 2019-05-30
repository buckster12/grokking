def sum(arr):
    if arr:
        return int(arr.pop())+sum(arr)
    else:
        return 0

print(sum([1, 2, 3, 4, 5, 11]))
