s = 'azcbobobegghakl'
numWord = 0
word = "bob"
for i in range(len(s) - len(word) + 1):
    #print("i :" + str(i) + "   a slovo nan je " + s[i])
    if s[i] == "b":
        sliceS = s[i:i+len(word)]
        #print(sliceS)
        if word == sliceS:
            numWord += 1

print("Number of times " + word + " occur is: " + str(numWord))
