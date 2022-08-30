# Online Python compiler (interpreter) to run Python online.
def selectionSort(a):
    for i in range(len(a)):
        min_idx=i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx=j
        a[min_idx], a[i]=a[i], a[min_idx]
    print("Selection Sort")
    print(a)
    return a
            
            
def bubbleSort(a):
    for i in range(len(a)):
        swapped= False
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]= a[j+1], a[j]
                swapped=True
        if swapped==False:
            break
    print("Bubble Sort")
    print(a)
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
                
        
    
arr = [64, 34, 25, 12, 22, 11, 90]
  
selectionSort(arr)
bubbleSort(arr)
insertionSort(arr)
            
# for i in range(3):
#     print(i)