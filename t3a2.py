lst = [('Tom',19,80),('John',20,90),('Jony',17,91),('Jony',17,93),('Json',21,85)]
def check(t1,t2):
    if t1[0] > t2[0]:
        return True
    elif t1[0] < t2[0]:
        return False
    else:
        if t1[1] > t2[1]:
            return True
        elif t1[1] < t2[1]:
            return False
        else:
            if t1[2] > t2[2]:
                return True
            else:
                return False
swapMade = True
count = len(lst)-1
while swapMade:
    swapMade = False
    for i in range(count):
        if check(lst[i],lst[i+1]):
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
            swapMade = True
    count -= 1
print(lst)
