def countEl(arr):
    if arr == []:
        return 0
    else:
        arr.pop()
        return 1 + countEl(arr)


print(countEl([1, 1, 1, 1, 1]))
