# Project 1. Guess the number with the minimum number of attempts.

## Table of Contents

1. [Project Description](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#project-description)
2. [What problem does it solve?](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#what-problem-does-it-solve)
3. [Brief information about the data](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#brief-information-about-the-data)
4. [Stages of work on the project](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#stages-of-work-on-the-project)
5. [Results](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#results)
6. [Conclusions](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#conclusions)

### Project Description

Guess the number guessed by the computer with the minimum number of attempts.

:arrow_up: [to the table of contents](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#table-of-contents)

### What problem does it solve?

You need to write a program that guesses the number with the minimum number of attempts.

**Competition conditions:**

- The computer guesses an integer from 0 to 100, and we need to guess it. By "guess," we mean "write a program that guesses the number."
- The algorithm considers whether the guessed number is larger or smaller than the one we need.

**Quality metric:**
Results are evaluated based on the average number of attempts per 1000 repetitions.

**What do we practice?**
Learning to write good code in Python

### Brief information about the data

The data consists of randomly generated numbers between 1 and 100. These numbers are used as the target numbers for the guessing algorithms. The performance of each algorithm is evaluated based on how many attempts it takes to correctly guess the target number.

### Stages of work on the project

1. Implement the `random_predict` function that randomly guesses numbers until it finds the correct one.
2. Implement the `game_core_v2` function that adjusts its guesses based on whether the guess is too high or too low.
3. Implement the `divide_predict` function that uses binary search to efficiently find the target number.
4. Create the `score_game` function to evaluate the performance of each guessing algorithm.
5. Run benchmarking tests to compare the effectiveness of each algorithm.

### Results

The results show the average number of attempts each algorithm takes to guess the target number over 10000 iterations.

### Conclusions

- The `random_predict` algorithm is the least efficient, taking the most number of attempts on average.
- The `game_core_v2` algorithm improves on `random_predict` by adjusting guesses based on feedback, reducing the number of attempts.
- The `divide_predict` algorithm is the most efficient, using a binary search approach to minimize the number of attempts needed to guess the target number.

:arrow_up: [to the table of contents](https://github.com/nikbeznosikov/sf_data_science/tree/main/project_1/README.md#table-of-contents)
