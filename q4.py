def stats_decorator(func):
    def wrapper(numbers):
        print("Numbers read:", numbers)
        print("Count:", len(numbers))
        print("Average:", sum(numbers) / len(numbers))
        print("Maximum:", max(numbers))
        func(numbers)
    return wrapper

@stats_decorator
def printStats(numbers):
    pass

# Example usage:
def read_data(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(float, line.split()))
            printStats(numbers)

# Example usage:
file_path = 'numbers_data.txt'  # Replace with the actual file path
read_data(file_path)
