# Import the product function from the itertools module
from itertools import product

# Define a function that generates double-word combinations from a file and writes them to another file
def generate_double_word_combinations(file_path, output_file_path):
    # Read the file and extract single words, stripping any leading or trailing whitespace
    with open(file_path, 'r') as file:
        single_words = [word.strip() for word in file.readlines()]

    # Generate all possible combinations of double words using the product function from itertools
    double_word_combinations = [''.join(combination) for combination in product(single_words, repeat=2)]

    # Write the combinations to the output file, separating each combination with a newline character
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(double_word_combinations))

# Example usage
# Define the input file path containing single words
input_file_path = '/home/sjain51/Desktop/Bonus_Project/dictionary.txt'

# Define the output file path where double-word combinations will be written
output_file_path = '/home/sjain51/Desktop/Bonus_Project/double_words_dictionary.txt'

# Call the function to generate double-word combinations and write them to the output file
generate_double_word_combinations(input_file_path, output_file_path)

