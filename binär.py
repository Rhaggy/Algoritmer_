import random
max = 200
min = -200
n = 5
lst = []
lst.append(random.randint(min,max))

print(range(n).lst)

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