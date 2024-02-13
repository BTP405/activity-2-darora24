def wordCount(file_path):
    word_line_mapping = {}

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase for better matching
                cleaned_word = word.strip('.,!?()[]{}"\'').lower()

                if cleaned_word not in word_line_mapping:
                    word_line_mapping[cleaned_word] = [line_number]
                else:
                    word_line_mapping[cleaned_word].append(line_number)

    return word_line_mapping

# Example usage:
file_path = 'text_file.txt'  # Replace with the actual file path
result = wordCount(file_path)
print(result)
