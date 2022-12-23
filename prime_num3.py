import math

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

def segmented_sieve(lower_limit, upper_limit):
    # Initialize a counter for the number of primes
    count = 0
    # Calculate the square root of the upper limit
    sqrt_upper_limit = int(math.sqrt(upper_limit))
    # Generate a list of primes up to the square root of the upper limit using the sieve of Eratosthenes
    primes = sieve_of_eratosthenes(2, sqrt_upper_limit)
    # Calculate the size of each segment
    segment_size = sqrt_upper_limit
    # Initialize the start and end of the current segment
    segment_start = lower_limit
    segment_end = segment_start + segment_size - 1
    # Loop until the end of the current segment is greater than the upper limit
    while segment_start <= upper_limit:
        # Create a list of all integers in the current segment
        segment = [i for i in range(segment_start, segment_end + 1)]
        # Iterate through the list of primes up to the square root of the upper limit
        for prime in primes:
            # Calculate the first multiple of the current prime that is greater than or equal to the start of the current segment
            first_multiple = math.ceil(segment_start / prime) * prime
            # Mark all multiples of the current prime in the current segment as non-prime
            for i in range(first_multiple, segment_end + 1, prime):
                if i in segment:
                    segment[i - segment_start] = None
        # Count the number of prime numbers in the current segment
        count += len([n for n in segment if n is not None])
        # Update the start and end of the next segment
        segment_start += segment_size
        segment_end += segment_size
    # Return the final count of prime numbers
    return count

# Example usage
count = segmented_sieve(1000000, 10000000)

