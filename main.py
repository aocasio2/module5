if guess = input("enter yopur guess:")
    print("you got it first time")
else:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
        guess = int(input())
        if guess == answer:
            print("well done, you guessed it")
        else:
            print("sorry, you have not guess correctly")
