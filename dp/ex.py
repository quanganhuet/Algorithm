## Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not.
## Both arrays are not in sorted order. It may be assumed that elements in both arrays are distinct.
arr1 = [11,1,13,21,3,7]
arr2 =[11,3,7,12]

def partition(arr, start, end):
    pivot= arr[end]
    i= start-1
    for j in range(start, end):
        if arr[j] < pivot:
            i=i+1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[end]= arr[end], arr[i+1]
    return i+1

def quicksort(arr,start, end):
    if start< end:
        middle=  partition(arr, start, end)
        quicksort(arr, start, middle-1)
        quicksort(arr, middle+1, end)
    return arr

quicksort(arr1,0, len(arr1)-1)
print(arr1)


quicksort(arr2,0, len(arr2)-1)
print(arr2)

def binarySearch(arr, value, start, end):
    if(start>end):
        return -1
    middle=(start+end)//2
    if arr[middle]== value:
        return middle
    if value > arr[middle]:
        return binarySearch(arr, value, middle+1, end)
    else:
        return binarySearch(arr, value, start, middle-1)
    
index= binarySearch(arr1, 21, 0, len(arr1)-1)
print(index)

def subArray(arr1, arr2):
    quicksort(arr1, 0, len(arr1)-1)
    quicksort(arr2, 0, len(arr2)-1)
    first_index= binarySearch(arr1, arr2[0], 0, len(arr1)-1)
    if first_index == -1:
        return False
    for j in range(1, len(arr2)):
        if arr2[j]!= arr1[j+first_index]:
            return False
    return True

print(subArray(arr1, arr2))
