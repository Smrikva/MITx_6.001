print("Please think of a number between 0 and 100!")
low = 0
high = 100

direction = "a"

while direction != "c":
    ans = int((low + high) * 0.5)
    print("Is your secret number {}?".format(ans))

    direction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is to low. Enter 'c' to indicate I guessed correctly.")
    
    
    if direction == "c":
        print("Game over. Your secret number was: {}".format(ans))
    elif direction == "l":
        low = ans
    elif direction == "h":
        high = ans
    else:
        print("Sorry, I did not understand your input.")

    
    
        
      
