
import random  
secret = random.randint(1, 100)  
attempts = 0                   
while attempts < 7:             
    guess = int(input("Your guess: "))
    attempts += 1            
    if guess == secret:
        print(f"Bravo! Found in {attempts} attempts")
        break 
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
if guess != secret:
    print("Lost! It was", secret)
