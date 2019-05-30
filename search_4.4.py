
def rec_search(arr, item, start=0):
    if(arr[start]-item == 0):
        return start
    else:
        start += 1
        return rec_search(arr, item, start)


my_list = [1, 2, 3, 5, 7, 9]

print(rec_search(my_list, 3))
print(rec_search(my_list, 9))
