def absSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            elif abs(arr[j]) == abs([j + 1]) and arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# TIme complexity is o(n^2) cause I'm using Bubble sort. 
# Using constant space though. 
