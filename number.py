#number guessing game
import random
def guess():
    print("Welcome to number guess game : ")
    lower=int(input("Enter lower bound : "))
    higher=int(input("Enter higher bound"))
    real_number=random.randint(lower, higher)
    print("You have 5 chances")
    attempts=0
    while attempts<5:
        attempts+=1
        number=int(input("Guess the number : "))
        if number==real_number:
            print(f"Yay! You guessed the number in {attempts} attempts.")
            break
        elif number>real_number:
            print("You guessed it too high")
        elif number<real_number:
            print("You guessed it too low")
    if attempts>=5:
        print(f"The number was {real_number}. Better luck next time!")
    print("Exited number guess game")
if __name__=="__main__":
    guess()