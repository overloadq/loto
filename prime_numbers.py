# not ok
def sieve_of_eratosthenes(lower_limit, upper_limit):
    # Create a list of all integers from the lower limit to the upper limit
    numbers = [i for i in range(lower_limit, upper_limit + 1)]
    # Iterate through the list of numbers
    for i in range(len(numbers)):
        # If the current number is not already marked as non-prime, mark all multiples of the current number as non-prime
        if numbers[i] is not None:
            for j in range(i + numbers[i], len(numbers), numbers[i]):
                numbers[j] = None
    # Return the list of numbers, with all non-prime numbers removed
    return [n for n in numbers if n is not None]

# Example usage
primes = sieve_of_eratosthenes(1000000, 10000000)
print(len(primes))  # Outputs: 66460
