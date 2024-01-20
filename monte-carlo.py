import random

def check_consecutive_blocks_and_numbers(sequence):
    # Sort the sequence in ascending order
    sequence.sort()

    # Initialize counters for consecutive blocks and consecutive numbers
    consecutive_block_count = 0
    consecutive_number_count = 0
    current_block = []

    # Check for consecutive blocks
    for i in range(len(sequence) - 1):
        if sequence[i] + 1 == sequence[i+1]:
            if not current_block:
                current_block = [sequence[i], sequence[i+1]]
            else:
                if sequence[i] == current_block[1]:
                    current_block[1] = sequence[i+1]
                else:
                    consecutive_block_count += 1
                    consecutive_number_count += current_block[1] - current_block[0] + 1
                    current_block = [sequence[i], sequence[i+1]]
        else:
            if current_block:
                consecutive_block_count += 1
                consecutive_number_count += current_block[1] - current_block[0] + 1
                current_block = []

    return consecutive_block_count, consecutive_number_count, 0  # Returning an additional placeholder value

def lottery_simulation(num_sims, num_draws):
    # Define the probability of each number being drawn
    prob = [1/49] * num_draws

    # Initialize counts for different cases
    no_consecutive_count = 0
    two_consecutive_count = 0
    three_consecutive_count = 0
    four_consecutive_count = 0
    five_consecutive_count = 0
    six_consecutive_count = 0
    one_block_count = 0
    two_block_count = 0
    three_block_count = 0

    # Simulate the lottery
    for i in range(num_sims):
        draw = random.sample(range(1, 50), num_draws)
        draw.sort()

        # Check for consecutive numbers
        consecutive_count = 1
        max_consecutive = 1
        for j in range(1, num_draws):
            if draw[j] == draw[j - 1] + 1:
                consecutive_count += 1
                max_consecutive = max(max_consecutive, consecutive_count)
            else:
                consecutive_count = 1

        # Update counts for different cases based on consecutive numbers found
        if max_consecutive == 1:
            no_consecutive_count += 1
        elif max_consecutive == 2:
            two_consecutive_count += 1
        elif max_consecutive == 3:
            three_consecutive_count += 1
        elif max_consecutive == 4:
            four_consecutive_count += 1
        elif max_consecutive == 5:
            five_consecutive_count += 1
        elif max_consecutive == 6:
            six_consecutive_count += 1

        # Check for consecutive blocks
        consecutive_block_count, _, _ = check_consecutive_blocks_and_numbers(draw)

        # Update counts for different cases based on consecutive blocks found
        if consecutive_block_count == 1:
            one_block_count += 1
        elif consecutive_block_count == 2:
            two_block_count += 1
        elif consecutive_block_count == 3:
            three_block_count += 1

    # Calculate probabilities for consecutive numbers
    total = num_sims
    no_consecutive_prob = no_consecutive_count / total
    two_consecutive_prob = two_consecutive_count / total
    three_consecutive_prob = three_consecutive_count / total
    four_consecutive_prob = four_consecutive_count / total
    five_consecutive_prob = five_consecutive_count / total
    six_consecutive_prob = six_consecutive_count / total

    # Calculate probabilities for consecutive blocks
    one_block_prob = one_block_count / total
    two_block_prob = two_block_count / total
    three_block_prob = three_block_count / total

    return (
        no_consecutive_prob, two_consecutive_prob, three_consecutive_prob,
        four_consecutive_prob, five_consecutive_prob, six_consecutive_prob,
        one_block_prob, two_block_prob, three_block_prob
    )

# Example usage
num_sims = 1000000
num_draws = 6

# Simulate the lottery and get the estimated probabilities
(
    no_consecutive_prob, two_consecutive_prob, three_consecutive_prob,
    four_consecutive_prob, five_consecutive_prob, six_consecutive_prob,
    one_block_prob, two_block_prob, three_block_prob
) = lottery_simulation(num_sims, num_draws)


# Print the estimated probabilities for consecutive numbers
print("The estimated probability of drawing zero consecutive numbers is:", no_consecutive_prob)
print("The estimated probability of drawing two consecutive numbers is:", two_consecutive_prob)
print("The estimated probability of drawing three consecutive numbers is:", three_consecutive_prob)
print("The estimated probability of drawing four consecutive numbers is:", four_consecutive_prob)
print("The estimated probability of drawing five consecutive numbers is:", five_consecutive_prob)
print("The estimated probability of drawing six consecutive numbers is:", six_consecutive_prob)

# Print the estimated probabilities for consecutive blocks
print("\nThe estimated probability of drawing one block is:", one_block_prob)
print("The estimated probability of drawing two blocks is:", two_block_prob)
print("The estimated probability of drawing three blocks is:", three_block_prob)
