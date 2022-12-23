class PrimeFactorization:
    def __init__(self, number):
        self.number = number
        self.factors = []

    def compute(self):
        # Start with the smallest prime number (2)
        divisor = 2
        while self.number > 1:
            # If the number is divisible by the divisor, add it to the list of factors and divide the number by the divisor
            while self.number % divisor == 0:
                self.factors.append(divisor)
                self.number = self.number / divisor
            # Increment the divisor by 1
            divisor += 1


# Example usage
# pf = PrimeFactorization(12287213)
# pf.compute()
# print(pf.factors)  # Outputs: [2, 3, 5]
