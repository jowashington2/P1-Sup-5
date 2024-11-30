import math
import random

def square_root(number):
    """
    Returns the square root of a number. Raises a ValueError if the number is negative.

    Parameters:
    number (float): The number to find the square root of.

    Returns:
    float: The square root of the number.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def random_integer_handler():
    """
    Picks a random integer between 1 and 100 (inclusive). Modifies or raises exceptions based on conditions.

    Returns:
    int: Modified or original integer based on conditions.
    """
    num = random.randint(1, 100)

    # Conditions
    if num % 2 != 0:  # If odd, multiply by 2
        num *= 2
    if num % 3 == 0:  # If divisible by 3, divide by 3
        num //= 3
    if num % 4 == 0:  # If divisible by 4, multiply by 4
        num *= 4
    if num > 4:  # If greater than 4, raise exception
        raise ValueError("Random number greater than 4.")
    
    return num


def divisible_by_input(number):
    """
    Takes an integer and returns a list of integers between 1 and 10 (inclusive) divisible by it.

    Parameters:
    number (int): The number to check divisors for.

    Returns:
    list: A list of integers divisible by the input number.
    """
    return [i for i in range(1, 11) if i % number == 0]
