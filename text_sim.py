# Filename: text_sim.py
# Author: Gabriel Sullivan

import math

allowed_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",  "S", "T", "U", "V", "W", "X", "Y", "Z", " "] # list of allowed characters

# Function name: standardize_text
# Purpose: special function designed to make all text into the same, consistent format
# Input: text - the text to standardize
#        standardize_letters - the allowed characters
# Output: the standardized text
# Raises: none
def standardize_text(text, standardize_letters):
    # Converts to lowercase
    lowercase_text = text.lower()
    # Removes punctuation
    no_punctuation_text = lowercase_text
    
    if standardize_letters == 1:
        no_punctuation_text = ""
        for letter in lowercase_text:
            is_allowed_letter = 0
            for other_letters in allowed_letters:
                if letter.lower() == other_letters.lower():
                    is_allowed_letter = 1
            
            if is_allowed_letter == 1:
                no_punctuation_text += letter
    return no_punctuation_text

# Function name: get_input
# Purpose: function designed to receive input from the user
# Input: prompt - the prompt to display
#        required_prompt - true if the input cannot be empty
# Output: the input received
# Raises: none
def get_input(prompt, required_prompt):
    # Loop that makes sure the user submits a text
    no_text_selected = 1
    while no_text_selected:
        print("")
        print(prompt)
        # Receives text input from the user
        return_text = str(raw_input())
        
        # If text is submitted, end the loop
        if return_text != "":
            no_text_selected = 0
        else:
            if required_prompt:
                no_text_selected = 1
            else:
                no_text_selected = 0
                return_text = ""
    return return_text

# Function name: print_intro
# Purpose: prints the intro text to the screen
# Input: none
# Output: none
# Raises: none
def print_intro():
    print("Welcome to the Text Similarity Test! Use this program to detect if two texts share some sort of connection.")
    print("")
    print("Once you submit two texts, the program will analyze the individual words and print out top word connections and their proximity. Then, it will offer a simple analysis.")
    print("")
    print("This program is useful for detecting plagiarism or another correlation between two texts.  For example, the program can show similarities between the Book of Mormon and the King James Bible. This would allow a user to further understand how the anthologies are related, and draw conclusions based on the data.")

print_intro() # Intro that guides the user

original_text_1 = get_input("To start, enter your first text.", 1)
original_text_1_standardized = standardize_text(original_text_1, 1) # Converts input to standard format that is easier to use
original_text_1_words = original_text_1_standardized.split() # Splits the string into words
original_text_2 = get_input("Now, enter your second text.", 1)
original_text_2_standardized = standardize_text(original_text_2, 1) # Converts input to standard format that is easier to use
original_text_2_words = original_text_2_standardized.split() # Splits the string into words
filter_input = get_input("Also, enter any words (separated by spaces) you would like the computer to filter out. Recommendations include \"and\", \"the\", \"is\", \"or\", \"a\", \"to\", \"of\", \"in\"", 0)
filter_input_standardized = standardize_text(filter_input, 0) # Converts input to standard format that is easier to use
outlawed_words = filter_input_standardized.split() # Splits the string into words

shared_words = {} # Declares the shared words list
original_text_1_word_position_dictionary = {} # Declares the first text's word position dictionary

# For loop that cycles through the first text and finds its position within the text, set based on the percent
# of the text that it is in, and stores it as a dictionary
i = 0
for word in original_text_1_words:
    percent_in_text = float(((i+1)/len(original_text_1_words))*100)
    original_text_1_word_position_dictionary[i] = {"position_percent":percent_in_text}
    i += 1

# Declares the second text's word position dictionary
original_text_2_word_position_dictionary = {}

# For loop that cycles through the second text and finds its position within the text, set based on the percent of the text that it is in
i = 0
for word in original_text_2_words:
    percent_in_text = float(((i+1)/len(original_text_2_words))*100)
    original_text_2_word_position_dictionary[i] = {"position_percent":percent_in_text}
    i += 1

i = 0
i2 = 0

# Goes through every single word in the first text
count_of_shared_words = 0
count_of_close_words = 0
for word in original_text_1_words:

    i2 = 0
    # Goes through each word in the second text per first word
    for second_word in original_text_2_words:
        # Finds out if the two words are the same
        if word == second_word:
            outlawed_word_alert = 0
            for outlawedword in outlawed_words:
                if word == outlawedword:
                      outlawed_word_alert = 1

            # Checks if it contains any of the filtered words. Skips if so
            if outlawed_word_alert == 0:
                # Finds the difference between the two same words based on their position in the percentage throughout the text.
                difference = abs(original_text_1_word_position_dictionary[i]["position_percent"] - original_text_2_word_position_dictionary[i2]["position_percent"])		
                count_of_shared_words += 1
                
                # If the difference is less than or equal to 10, the program assumes the words are related and adds it to a counter of the close words
                if difference <= 10:
                      count_of_close_words += 1
        i2 += 1

    i += 1

# Formatting designed to improve user experience
print("")

print("--------------------------------------------------")

print("")

# If statement makes sure we do not divide by zero
if count_of_shared_words != 0:
    # Finds how many words are considered to be related by the program
    percent_of_close_words = (float(count_of_close_words)/float(count_of_shared_words))*100
else:
    percent_of_close_words = 0

# Prints output of the percentage
print("About "+str(int(percent_of_close_words))+"% of shared words are within the same region of the texts (error of 5%).")

# Program provides simple analysis. if the percentage is greater than 30%, then the program presumes the texts are related, otherwise, not.
if percent_of_close_words > 30:
    print("The two texts are likely related.")
else:
      print("The two texts are not likely related.")
