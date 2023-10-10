def MergeSort(arr):
    if len(arr) > 1:
 
        middle = len(arr)//2
 
        L = arr[:middle]
        R = arr[middle:]
        MergeSort(L)
        MergeSort(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
        if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
        else:
                arr[k] = R[j]
                j += 1
        k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
def PrintSortedList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
PrintSortedList(arr)
MergeSort(arr)
print("Sorted array is: ", end="\n")
PrintSortedList(arr)
