

lst = [23,65,323,12,43,34,76,87,34,23,45,33412,223,56,78,]


x = 34
 
def bin_search(lst, x):
    start = 0 
    stop = len(lst) -1
    while stop > start:
        mid = (start + stop) // 2
        if x == lst[mid]:
            return mid
        elif x > lst[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return -1