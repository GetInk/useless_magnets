def sortarray(array):
    Sorted = []
    Range = True
    for biggest in array:
        if Range == True:
            Range = biggest
        else:
            if Range < biggest:
                Range = biggest
    for amount in range(0, Range):
        Sorted.append(0)
    for i in array:
        Sorted[i-1] += 1
    x = []
    for n in range(0, Range):
        for o in range(0, Sorted[n]):
            x.append(n+1)
    return x

def bubble(array):
    Sorted = array
    finish = False
    while finish == False:
        finish = True
        for amount in range(0, len(Sorted)-1):
            if Sorted[amount] > Sorted[amount+1]:
                x = Sorted[amount]
                Sorted[amount] =  Sorted[amount+1]
                Sorted[amount+1] = x
                finish = False
    return Sorted

def mush(array):
    Sorted = array