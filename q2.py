import matplotlib.pyplot as plt

def graphSnowfall(file_path):
    # Read data from the file
    with open(file_path, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file]

    # Aggregate data into 10 cm ranges
    snowfall_ranges = [0] * 6  # Ranges: 0-10, 11-20, 21-30, 31-40, 41-50, 51+
    for amount in snowfall_data:
        index = min(amount // 10, 5)  # Determine the index for the range
        snowfall_ranges[index] += 1

    # Plotting the bar graph
    ranges_labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51+']
    plt.bar(ranges_labels, snowfall_ranges, color='skyblue')
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.show()

# Example usage:
file_path = 'snowfall_data.txt'  # Replace with the actual file path
graphSnowfall(file_path)
