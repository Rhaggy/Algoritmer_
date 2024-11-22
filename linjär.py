def lin_sökning(numbers , t):
    for i in range(len(numbers)):
        if t == numbers[i]:
            return i
    return -1


numbers = [1,2,3,4,5,6,7,8,9, 10]

t = 4

        
print(lin_sökning(numbers, t ))