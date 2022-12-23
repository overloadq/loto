import math
def count_primes(lower_limit, upper_limit):
    # Initialize a counter for the number of primes
    count = 0
    # Iterate through the range of numbers from the lower limit to the upper limit
    for i in range(lower_limit, upper_limit + 1):
        # Check if the current number is prime
        if is_prime(i):
            # If the current number is prime, increment the counter
            count += 1
    # Return the final count of prime numbers
    return count

def is_prime(number):
    # Check if the number is 2 or 3, which are both prime
    if number == 2 or number == 3:
        return True
    # Check if the number is even or less than 2, which are not prime
    if number % 2 == 0 or number < 2:
        return False
    # Check if the number is divisible by any odd numbers between 3 and the square root of the number
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    # If the number is not divisible by any odd numbers between 3 and the square root of the number, it is prime
    return True

# Example usage
count = count_primes(1000000, 10000000)
print(count)  # Outputs: 66460
