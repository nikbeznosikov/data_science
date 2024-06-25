import numpy as np

def random_predict(number: int = 1) -> int:
    """Simply guess randomly, without using information about whether it is more or less.
       The function accepts the guessed number and returns the number of attempts

    Args:
        number (int, optional): The guessed number. Defaults to 1.

    Returns:
        int: The number of attempts
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # the guessed number
        if number == predict_number:
            break  # exit the loop if guessed correctly
    
    return count
  
def game_core_v2(number: int = 1) -> int:
    """First, set any random number, and then decrease
    or increase it depending on whether it is more or less than the required one.
       The function accepts the guessed number and returns the number of attempts
       
    Args:
        number (int, optional): The guessed number. Defaults to 1.

    Returns:
        int: The number of attempts
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count
  
def score_game(random_predict) -> int:
    """How many attempts on average does our algorithm guess in 10000 approaches

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(10000))  # guessed list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in: {score} attempts")
    
    
def divide_predict(number: int = 1) -> int:
    """Predicts the number by dividing the range in half each time.

    Args:
        number (int, optional): The guessed number. Defaults to 1.

    Returns:
        int: The number of attempts
    """
    
    count = 0
    start = 1
    end = 101
    predict = (start + end) // 2
    
    while number != predict:
        count += 1
        
        if number > predict:
            start = predict
        elif number < predict:
            end = predict
            
        predict = (start + end) // 2

    return count
    
    
# Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
score_game(random_predict)

print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)

print('Run benchmarking for divide_predict: ', end='')
score_game(divide_predict)
