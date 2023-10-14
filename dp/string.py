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

        
    
print(makeAnagram("cde", "dcf"))

