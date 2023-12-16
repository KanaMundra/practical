import string

# Define the string with punctuation
text = "This, string! has? some #punctuation."

# Define punctuation to remove
punctuations = string.punctuation

# Remove punctuation using translate() with a mapping table
no_punct = text.translate(str.maketrans('', '', punctuations))

# Print the original and modified string
print(f"Original: {text}")
print(f"Without punctuation: {no_punct}")
