import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): The guessed number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 500)  # assumed number
        if number == predict_number:
            break  # exit the loop if guessed correctly
    return count


def score_game(random_predict) -> int:
    """On average, how many attempts does our algorithm take to guess the number in 1000 runs

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = []  # list to save the number of attempts
    np.random.seed(1)  # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # guessed a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # find the average number of attempts

    print(f"Your algorithm guesses the number on average in: {score} attempts")
    return score


# RUN
if __name__ == "__main__":
    score_game(random_predict)
