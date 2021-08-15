def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return theSeq

el = [342, 21, 2, 456, 23, 0, 67, 56, 3, 7]

result = bubbleSort(el)

print(result)
