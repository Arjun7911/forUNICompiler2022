import random
num = random.randint(1, 10)

guess1 = int(input("Enter your first guess : "))

if (guess1 != num):
    print("Incorrect guess")
    print("Your Current Score : 2/3")
    
    if (num % 2 == 0):
        print("HINT1 : The number is even")
    else:
        print("HINT1 : The number is odd")
    
    guess2 = int(input("Enter your second guess : "))
    
    if (guess2 != num):
        print("Incorrect guess")
        print("Your Current Score : 1/3")
        
        if (num>5):
            print("HINT2 : The number is greater than 5")
        else:
            print("HINT2 : The number is less than 6")
    
        guess3 = int(input("Enter your final guess : "))
        
        if (guess3 != num):
            print("Incorrect guess")
            print("Your Current Score : 0/3")
        
        else:
            print("Correct guess")
            print("Your Score : 1/3")
    
    else:
        print("Correct guess")
        print("Your Score : 2/3")
    
else:
    print("Correct guess")
    print("Your score : 3/3")
