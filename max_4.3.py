def maxEl(arr):
    if(len(arr) == 1):
        return arr[0]

    if(arr[0] > arr[1]):
        arr.pop(1)
    else:
        arr.pop(0)
    return maxEl(arr)


print(maxEl([1, 1, 31, 4, 5, 12, 9]))
