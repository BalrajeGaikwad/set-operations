# Accept input from the user
input_text = input("Enter a sequence of whitespace-separated words: ")

# Split the input into words and remove duplicates using a set
unique_words = set(input_text.split())

# Sort the words alphanumerically
sorted_words = sorted(unique_words)

# Join the sorted words into a single string and print the result
output_text = " ".join(sorted_words)
print(output_text)
