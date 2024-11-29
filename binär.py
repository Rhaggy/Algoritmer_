lst = [12,34,778,34,6752,3,562,324,7534,6754,67,54789,99]

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