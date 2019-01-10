def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels = ("a", "e", "i", "o", "u")
    withoutVowels = ""
    for char in s:
        if char.lower() in vowels:
            continue
        else:
            withoutVowels += char
            
    print(withoutVowels)
