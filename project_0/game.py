import numpy as np

number = np.random.randint(1, 101)  # guessing the number
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100"))

    if predict_number > number:
        print("The number should be smaller!")

    elif predict_number < number:
        print("The number should be bigger!")

    else:
        print(f"You guessed the number! This number is {number}, in {count} attempts")
        break  # end of the game, exit the loop
