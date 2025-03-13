def evenFirst(arr):
    evenIndex = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenIndex] = arr[evenIndex], arr[i]
            evenIndex += 1
    return arr
print(evenFirst(a))
