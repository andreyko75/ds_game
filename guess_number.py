"""Guess the number game
The computer itself guesses and itself guesses the number in the minimum number of moves
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Guess the number

    Args:
        number (int, optional): Guess number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    min_num, max_num = 1, 101
    while True:
        count += 1
        predict_number = (min_num + max_num) // 2  # Estimated number, half method
        if number == predict_number:
            break  # Exit from the loop if the number is guessed
        if predict_number < number:
            min_num = predict_number
        else:
            max_num = predict_number

    return count


def score_game(rand_predict) -> int:
    """For what number of attempts on average for 1000 approaches our algorithm guesses

    Args:
        rand_predict ([type]): guess function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=1000)  # Мake a list of numbers

    for number in random_array:
        count_ls.append(rand_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in: {score} attempts on average")
    return score


if __name__ == "__main__":
    # Run
    score_game(random_predict)
