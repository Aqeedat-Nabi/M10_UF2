import random

def guess_the_number():
    num = random.randint(1,100)
    attempt = 0
    
    print(" Choose a number between 1 & 100 ")
    
    while True:
        user_num = int(input("Guess a number : "))
        attempt += 1
        
        if user_num == num:
            print(f"You guessed the correct number : {user_num} in {attempt} attempts .")
            break
        elif user_num < num:
            print(f"The number you guessed is smaller than the actual number : {user_num} Try a larger one.. in {attempt} attempts .")
        else:
            print(f"The number you guessed is greater than the actual number : {user_num} Try a smaller one.. in {attempt} attempts .")

if __name__ == '__main__':
    guess_the_number()