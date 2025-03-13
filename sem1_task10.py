def grades(arr):
    left = 0
    right = 1
    while right != len(arr):
        if (arr[left] == 0) and (arr[right] != 0):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right += 1
        elif arr[left] == 0:
            right += 1
        else:
            left += 1
    return arr
print(grades(a))
