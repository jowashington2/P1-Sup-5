# P1-Sup-5
Programming Languages 

# Project 1 Supplement – 5

## Objective
To implement Python functions with proper testing and documentation.

## Functions Implemented
1. `square_root(number)`
   - Returns the square root of a number.
   - Raises a `ValueError` if the number is negative.

2. `random_integer_handler()`
   - Picks a random integer between 1 and 100 and applies conditions:
     - If odd, multiply by 2.
     - If divisible by 3, divide by 3.
     - If divisible by 4, multiply by 4.
     - If greater than 4, raises a `ValueError`.

3. `divisible_by_input(number)`
   - Returns a list of integers between 1 and 10 divisible by the input number.

## Testing
- Unit tests are included for all functions.
- Run the tests with:
  ```bash
  python -m unittest discover tests
