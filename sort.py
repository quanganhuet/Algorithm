# Online Python compiler (interpreter) to run Python online.
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L= arr[:mid]
        R= arr[mid:]
        i=j=k=0
        mergeSort(L)
        mergeSort(R)
        while i< len(L) and j< len(R):
            if L[i] < R[j]:
                arr[k] =L[i]
                i=i+1
            else:
                arr[k]= R[j]
                j=j+1
            k=k+1
        while i < len(L):
            arr[k]= L[i]
            i=i+1
            k=k+1
        while j< len(R):
            arr[k] = R[j]
            j=j+1
            k=k+1
        
def quickSort(arr, low, high):
        if(low< high):
            pivot_index=partition(arr, low, high)
            quickSort(arr, low, pivot_index-1)
            quickSort(arr, pivot_index+1, high)


def partition(arr, low, high):
    pivot = arr[high]
    # variable i to control what position in list smaller than pivot 
    i= low-1
    for j in range(low, high):
        if arr[j]< pivot:
            i=i+1
            arr[i], arr[j]= arr[j], arr[i]
    arr[i+1], arr[high]= arr[high], arr[i+1]
    return i+1
# quickSort(arr, 0, len(arr)-1)       


        
# Time complexity O(n)
# Auxiliary space O(1)
def selectionSort(a):
    for i in range(len(a)-1):
        min_idx=i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx=j
        a[min_idx], a[i]=a[i], a[min_idx]
    print("Selection Sort")
    print(a)
    return a
            
            
def bubbleSort(a):
    for i in range(len(a)-1):
        swapped= False
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]= a[j+1], a[j]
                swapped=True
        if swapped==False:
            break
    print("Bubble Sort")
    return a
    
def insertionSort(a):
    for i in range(1, len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key < a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    print("Insetion Sort")
    print(a)
    return a


def binarySearch(index, arr, first, end):
    if(first> end):
        return 'Not found'
    middle = (first+end)//2
    if (index==arr[middle]):
        return middle
    elif (index > arr[middle]):
        return binarySearch(index, arr, middle+1, end)
    else :
        return binarySearch(index, arr, first, middle-1)

def binarySearchNotRecursion(index, arr, first, end):
    while (first<end):
        middle = (first+end)//2
        if (index==arr[middle]):
            return middle
        elif (index > arr[middle]):
            first = middle+1
        else:
            end= middle-1
    return "Not found"
arr = [64, 34, 25, 12, 22, 11, 90,30,-1, -8, 60, 50, 100,99]
  
# selectionSort(arr)
# bubbleSort(arr)
# insertionSort(arr)
# mergeSort(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)
print(binarySearchNotRecursion(65, arr, 0, len(arr)-1))
# res = binarySearch(64, arr, 0, len(arr)-1)
# print(res)


