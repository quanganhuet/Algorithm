# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine 
# and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note 
# are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words 
# from the magazine; otherwise, print No.
import hashlib

magazine= "o l x imjaw bee khmla v o v o imjaw l khmla imjaw x"
note= "imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o"


magazine= magazine.rstrip().split()
note=note.rstrip().split()
def checkMagazine2(magazine, note):
    hashset = set()
    for i in range(len(magazine)):
        hashset.add(magazine[i])
    for i in range(len(note)):
        if note[i] in hashset:
            continue
        else:
            return 'No'
    return 'Yes'

def checkMagazine1(magazine, note):
    magazineCount={}
    noteCount={}
    hashset = set()
    for i in range(len(magazine)):
        if(magazine[i] in magazineCount):
            magazineCount[magazine[i]]= magazineCount[magazine[i]]+1
        else:
            magazineCount[magazine[i]]=0
        hashset.add(magazine[i])
    
    p= len(hashset)
    for i in range(len(note)):
        if(note[i] in noteCount):
            noteCount[note[i]]= noteCount[note[i]]+1
        else:
            noteCount[note[i]]=0
        hashset.add(note[i])

    if (len(hashset)==p):
        for i in range(len(note)):
            if(noteCount[note[i]]> magazineCount[note[i]]):
                return 'No'
        return 'Yes'
    else:
        return 'No'

print(magazine)
print(checkMagazine1(magazine, note))