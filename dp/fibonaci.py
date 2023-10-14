import time
def fib(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+ fib(n-2)

def fib2(n, memo={}):
    if n in memo:
        return memo[n]
    if (n==0):
        result = 0
    elif(n==1):
        result = 1
    else:
        result = fib2(n-1, memo)+ fib2(n-2, memo)
    memo[n]= result
    return memo[n]

# Time complexity 0(n)
# Auxilary space O(n)
def fib3(n):
    fib=[0,1]
    for i in range(2, n+1):
        fib[i] = fib[i-1]+ fib[i-2]
    return fib[n]

def fib4(n):
    a=0
    b=1
    if (n==0):
        return a
    elif(n==1):
        return b
    else
        for i in range(2, n+1)
            c=a+b
            a=b
            b=c
        return b

start_time = time.time()
print(fib(30))
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time v1: ", elapsed_time)

start = time.time()
print(fib2(30))
end = time.time()
elapsed_time = end - start
print("Elapsed time v2: ", elapsed_time)

start = time.time()
print(fib3(30))
end = time.time()
elapsed_time = end - start
print("Elapsed time v3: ", elapsed_time)