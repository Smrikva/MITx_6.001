s = "aaaaaaassssxddfeasdasdwwassdfasdfffs"
alphabet = "abcdefghijklmnopqrstuvwxyz"

stringAlphabet = ""
longestStringAlphabet = ""
counter = 0
while True:
    if counter == len(s):
        break
    
    #if index1 less than index2, append letter to form a string
    #else continue from next letter
    index1 = alphabet.index(s[counter])
    if counter == len(s)-1:
        index2 = index1 -1
    else:
        index2 = alphabet.index(s[counter + 1])

    
    stringAlphabet += s[counter]
    if index1 > index2:
        if len(longestStringAlphabet)<len(stringAlphabet):
            longestStringAlphabet = stringAlphabet
        stringAlphabet = ""
        #break if not enough letters remain
        if len(longestStringAlphabet) > len(s[counter:]):
            break
        
    counter += 1    

print(longestStringAlphabet)






