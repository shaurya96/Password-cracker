# Define the starting number for the range of numbers to be written to the file
start_number = 999

# Define the ending number (inclusive) for the range of numbers to be written to the file
end_number = 99999999

# Specify the file path where the numbers will be written
output_file_path = 'numbers.txt'

# Open the file specified by output_file_path in write ('w') mode
# The 'with' statement ensures that the file is properly closed after writing
with open(output_file_path, 'w') as file:

    # Iterate through each number in the specified range
    for number in range(start_number, end_number + 1):

        # Convert the current number to a string and write it to the file
        # Append a newline character ('\n') after each number to separate them
        file.write(str(number) + '\n')

  
  #Same code can be used to generate numbers1.py which has range 9-9999 and is used in cracking single word and number(COMBINED) password.
