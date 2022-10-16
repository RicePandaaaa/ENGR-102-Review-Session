"""
Given a list of words stored in the variable List_words, output the longest word and the length of the longest
word (assume that there will be only 1 word of the longest length). Output may look like:

The longest word "champions" has 9 characters.
"""

# Given list of words
List_words = ["tony", "pt", "champions", "league", "grass", "badjokes"]

# Store data
longest_word = ""
longest_length = 0

# Loop through each word and compare against the current longest word
for word in List_words:
    # Compare and update as necessary
    if len(word) > longest_length:
        longest_word = word
        longest_length = len(word)

# Output
print(f'The longest word "{longest_word}" has {longest_length} characters.')