import random 
import numpy as np
import matplotlib.pyplot as plt


def bogoSort(lst):
    n = len(lst)
    while (is_sorted(lst)== False):
        shuffle(lst)

def is_sorted(lst):
    n = len(lst)
    for i in range(0, n-1):
        if (lst[i] > lst[i+1] ):
            return False
    return True

def shuffle(lst):
    n = len(lst)
    for i in range (0,n):
        r = random.randint(0,n-1)
        lst[i], lst[r] = lst[r], lst[i]

lst = [3, 2, 4, 1, 0, 5]
bogoSort(lst)


print("Sorted array :")
for i in range(len(lst)):
    print ("%d" % lst[i]),

plt.show

