##Given an integer array of coins[ ] of size N representing different types of currency and an integer sum,
## The task is to find the number of ways to make sum by using different combinations from coins[].

import time

coins=[3,2,1]

## Time complexity O(n)
## Auxiliary Space O(1)
def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        swapped=False
        for j in range(0, len(arr)-1-i):
            if(arr[j]<arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if swapped==False:
            break

def insertionSort(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while (key< arr[j] and j>0):
            arr[j+1] =arr[j]
            j=j-1
        j=j+1
        arr[j] = arr[key]

def selectionSort(arr):
    for i in range(0, len(arr)-1):
        min_idx=i
        for j in range(i+1, len(arr)):
            if a[min_idx] < a[j]:
                min_idx=j
        a[i], a[min_idx]= a[min_idx], a[i]

def mergeSort(arr):
    if len(arr)>1:
        middle= len(arr)//2
        l=arr[:middle]
        r=arr[middle:]
        i=j=k=0
        mergeSort(l)
        mergeSort(r)
        while (i< len(l) and (j<len(r))):
            if arr[i]<arr[j]:
                arr[k]=arr[i]:
                i=i+1
            else:
                arr[k]=arr[j]:
                j=j+1
            k=k+1
        while i < len(l):
            arr[k]=arr[i]
            i=i+1
            k=k+1
        while j < len(r):
            arr[k]=arr[j]
            j=j+1
            k=k+1


bubbleSort(coins)
print(coins)
def coinChange(sum, coins):


