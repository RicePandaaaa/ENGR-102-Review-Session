"""
Given a list of words stored in the variable List_words, output the longest word and the length of the longest
word (assume that there will be only 1 word of the longest length). Output may look like:

The longest word "champions" has 9 characters.
"""

# List of words
List_words = ["Frodo", "Anthony", "champions", "discord", "engr102"]

# Data variables
longest_length = 0
longest_word = ""

# Loop
for word in List_words:
    # Compare current word to current longest
    if len(word) > longest_length:
        # Update the values
        longest_length = len(word)
        longest_word = word

print(f'The longest word "{longest_word}" has {longest_length} characters.')