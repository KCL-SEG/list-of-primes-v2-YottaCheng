"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")

    list_of_primes = []
    num = 2
    while len(list_of_primes) < number_of_primes:
        if all(num % prime != 0 for prime in list_of_primes):
            list_of_primes.append(num)
        num += 1

    return list_of_primes
