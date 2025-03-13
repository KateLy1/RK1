def isSubsequence(a, b):
    i = 0
    lenA = len(a)
    lenB = len(b);

    for el1 in range(lenA):
        for el2 in range(lenB):
            if (a[el1] == b[el2]):
                i += 1
                break
    return i == lenA

print(isSubsequence(a, b))
