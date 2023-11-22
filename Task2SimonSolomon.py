'''
Name: Simon Solomon
Due Date: 11/20/23
Assignment: Ch7 Lab 2
Description: Create a program to reads and outputs words from a file 
Academic Honesty Pledge: I, Simon, do hereby certify that I have derived no assistance for this project from any sources other than those listed
as references
References : 

'''

# Task 1

# Open the file in read mode
poem = open("poem.txt", "r")
# Read the contents of the file and store it in the variable
poem_text = poem.read()
# Split the contents of the poem into individual words
words = poem_text.split()
# Iterate through the list of words and print each word
for word in words:
    print(word)
    
# Task 2
count = 0

# Reopen the file to start reading from the beginning
poem = open("poem.txt", "r")

char = poem.read(1)

# Start a while loop that continues as long as there are characters to read
while char:
    # Print the current character
    print(char, end="")
    count += 1
    # Read the next character from the file
    char = poem.read(1)

# Close the file after reading
poem.close()

# Print the total count
print("\nTotal character count: ", count)



    