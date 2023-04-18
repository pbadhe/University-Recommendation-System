# Open the text file
with open('data/Universities.txt', 'r') as f:
    # Loop through each line in the file
    for line in f:
        # Remove any extra whitespace (like newlines) from the line
        line = line.strip()
        # Print the university name
        print(line)
