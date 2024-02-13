def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """Function to generate a list of prime numbers between 2 and n."""
    return [num for num in range(2, n+1) if is_prime(num)]

# Example usage:
n = 20
result = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {result}")
