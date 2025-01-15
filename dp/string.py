# A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the 
# first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the 
# same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character 
# deletions required to make the two strings anagrams. Determine this number.

# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to 
# make a and b anagrams. Any characters can be deleted from either of the strings.


def makeAnagram(a, b):
    arrayA= list(a)
    arrayB= list(b)
    checkList={}  
    count=0
    for index, item in enumerate(arrayA):
        if(item in checkList):
            checkList[item]["a"]=checkList[item]["a"]+1
        else:
            checkList[item]={"a":1, "b":0}
    for index, item in enumerate(arrayB):
        if(item in checkList):
            checkList[item]["b"]=checkList[item]["b"]+1
        else:
            checkList[item]={"b":1, "a":0}
    for key, value in checkList.items():
        count = count+ abs(checkList[key]["a"]-checkList[key]["b"])
    return count

        
    
# print(makeAnagram("cde", "dcf"))

# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. 
# On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

# Given the value of "money" and the "cost" of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct 
# flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a cost. 
# For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated 
# integers on a new line. You must print the smaller ID first and the larger ID second.

# Example:
# cost=[2,1,3,5,6]
# money=5
# They would purchase flavor ID's 1 and 3 for a cost of 2+3=5. Use 1 based indexing for your response.

# def whatFlavors(cost, money):
    # Write your code here



# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    dimension = len(arr[0])
    diag1=0
    diag2=0
    for x in range(dimension):
        diag1=diag1+arr[x][x]
        diag2=diag2+arr[dimension-x-1][x]
    return abs(diag1-diag2)

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    negative, positive, zero=0,0,0
    for item in arr:
        if item> 0:
            positive=positive+1
        elif item<0:
            negative=negative+1
        else:
            zero=zero+1
    negativeRatio= round(negative / len(arr), 6)
    positiveRatio= round(positive / len(arr), 6)
    zeroRatio= round(zero / len(arr), 6)
    print(f"{positiveRatio:.6f}")
    print(f"{negativeRatio:.6f}")
    print(f"{zeroRatio:.6f}")



# plusMinus([-4,3,-9, 0,4,1])

##Staircase detail

# This is a staircase of size : 4
  #
  ##
 ###
####

def staircase(n):
    for i in range(n):
        print((n-i-1)*" "+(i+1)*"#")

# staircase(5)

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    arr.sort()
    sum=0
    for item in arr:
        sum=sum+item
    max= sum-arr[0]
    min= sum-arr[len(arr)-1]
    print(f"{min} {max}")

# miniMaxSum([-4,3,-9, 0,4,1])

    
# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
#  They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

def birthdayCakeCandles(candles):
    candles.sort()
    print(candles)
    max= candles[-1]
    count=0
    for i in range(len(candles)-1, -1, -1):
        if candles[i]==max:
            count= count+1
        else:
            break
    return count
candles=[4,3,2,4]
# print(birthdayCakeCandles(candles))


s = "AAAAAB"
def alternatingCharacters(s):
    index=0
    count=0
    for i in range(1, len(s)):
        if(s[i]!=s[index]):
            index=i
        else:
            count=count+1
    return count


# alternatingCharacters(s)


# def isValid(s):
#     fre=[]
#     for i in range(len(s)):
#         if in fre:
#             fre[i]=fre[i]+1
#         else:
#             fre[i]= fre[0]
            

#     # Write your code here



def twoStrings(s1, s2):
    dict1={}
    for c in s1:
        if c not in dict1:
            dict1[c] = 1
    for c in s2:
        if dict1.get(c):  # Use dict1 and check for the character c in s2
            return 'YES'
    return 'NO'

s1='hello'
s2='world'
twoStrings(s1,s2)


#Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
#$ Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
# Example

ifailuhkqq
[1]

45
kkkk

kk
[0,1] [1,2] [2,3] 

[0] [1] [2] [3]

[0,1,2] [1,2,3]
10
def sherlockAndAnagrams(s):
    dicta={}
    for c in s:
        dicta[c]
        