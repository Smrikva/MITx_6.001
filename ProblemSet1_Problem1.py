s = 'azcbobobegghakl'
numVowels = 0
vowels=["a", "e", "i", "o", "u"]
for letter in s:
	if letter in vowels:
		numVowels += 1

print("Number of vowels: " + str(numVowels))
