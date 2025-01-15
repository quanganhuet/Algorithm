# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
# You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
# 1 3 5 2 4 6 7

# 1 2 5 3 4 6 7 

# 1 2 3 5 4 6 7

# 1 2 3 4 5 6 7 

# 4 3 1 2

# 1 3 4 2

# 1 2 4 3

# 1 2 3 4
arr0=[1,3,5,2,4,6,7]
arr1=[4,3,1,2]

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

def findMinimumOfSwaps(arr):
    count=0
    maxLength= len(arr)
    newArray= arr[0:maxLength]
    quickSort(newArray, 0, maxLength-1)
    for index in range(maxLength):
        smallestIndex= index
        swapIndex=index
        smallest= arr[index]
        swapIndex = binarySearch(smallest,newArray,0, maxLength)
        print(swapIndex)
        if (smallestIndex!= swapIndex):
            arr[smallestIndex], arr[swapIndex] = arr[swapIndex], arr[smallestIndex]
            count=count+1
    return count


# checkIndex= [0,1,2,3,4,5,6]
def minimumSwaps(arr):
    count=0
    n= len(arr)
    checkIndex = []
    for i in range(0, n):
        checkIndex.append(i)
    lp=0
    while(lp<n):
        if(checkIndex[lp]!=-1):
            itemWantToKnowLocation= checkIndex[lp]
            itemAtThatLocation = arr[itemWantToKnowLocation]
            if (itemAtThatLocation != lp+1):
                exactLocation= itemAtThatLocation-1
                arr[itemWantToKnowLocation], arr[exactLocation] = arr[exactLocation], arr[itemWantToKnowLocation]
                count=count+1
                checkIndex[exactLocation]=-1
            else:
                checkIndex[lp]=-1
                lp=lp+1
        else:
            lp=lp+1
    
    return count

print(minimumSwaps(arr1))
print(arr1)


#Starting with a 1-indexed array of zeros and a list o f operations, for each operation add a value to each the array element between two given indices, 
#inclusive. Once all operations have been performed, return the maximum value in the array.
##5 3
# 1 2 100
# 2 5 100
# 3 4 100
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER ndawdasdawdsdawdadwdadadadadadadadadwdsdawdasdawdaadwdasdadawdawdasdawd
#  2. 2D_INTEGER_ARRAY queries
#
n=5
queries = [[1,2,100],[2,5,100],[3,4,100]]
n2=4
queries2= [[2,3,603],[1,1,286],[4,4,882]]

def arrayManipulation(n, queries):
    array = [0]*n
    rows= len(queries)
    for row in range(rows):
        for i in range((queries[row][0]-1), (queries[row][1])):
            array[i]=array[i]+ queries[row][2]
    return max(array)
    # Write your code here 
print(arrayManipulation(n2, queries2))


def initializedDiffArray(A):
    n= len(A)

    D= [0 for i in range(0, n+1)]

    D[0] = A[0]
    D[n] = 0

    for i in range(1,n):
        D[i]= A[i] - A[i-1]
    return D

def update(D, l, r, x)
    D[l] += x 
    D[r+1] -= x

def printArray(A,D):
    for i in range(0, len(A)):
        if(i==0):
            A[i]= D[i]
        else:
            A[i]= D[i]+A[i-1]


