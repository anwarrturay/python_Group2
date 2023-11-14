guess_number = int(input("Enter guess  number ranging 1 to 5: "))
user_move = int(input("Enter a number ranging 1 to 5: "))


if(guess_number>0 and guess_number <= 5):
    if(user_move == guess_number):
        print("Your guess is correct")
    elif(user_move != guess_number):
        for i in range(5):
            print("Your guess is wrong")
            user_move = int(input("Please try again: "))
            if(user_move == guess_number):
                print("Your guess is correct")  
                break
        else:
            print("You've reached the limit of guessing")
            


else:
    print("Invalid input")
