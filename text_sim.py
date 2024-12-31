#Imports Math expressions
import math

allowed_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",  "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

#special function designed to make all text into the same, consistent format
def standardizetext(text, standardize_letters):
	#converts to lowercase
	lowercase_text = text.lower()
	#removes punctuation
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

#function designed to receive input from the user
def getinput(prompt, required_prompt):
	#loop that makes sure the user submits a text
	no_text_selected = 1
	while no_text_selected:
		print("")
		print(prompt)
		#Receives text input from the user
		return_text = str(raw_input())
		
		#if text is submitted, end the loop
		if return_text != "":
			no_text_selected = 0
		else:
			if required_prompt:
				no_text_selected = 1
			else:
				no_text_selected = 0
				return_text = ""
	return return_text

#Intro that guides the user
print("Welcome to the Text Similarity Test! Use this program to detect if two texts share some sort of connection.")

print("")

print("Once you submit two texts, the program will analyze the individual words and print out top word connections and their proximity. Then, it will offer a simple analysis.")

print("")

print("This program is useful for detecting plagiarism or another correlation between two texts.  For example, the program can show similarities between the Book of Mormon and the King James Bible. This would allow a user to further understand how the anthologies are related, and draw conclusions based on the data.")

original_text_1 = getinput("To start, enter your first text.", 1)

#Converts input to standard format that is easier to use
original_text_1_standardized = standardizetext(original_text_1, 1)

#Splits the string into words
original_text_1_words = original_text_1_standardized.split()

original_text_2 = getinput("Now, enter your second text.", 1)

#Converts input to standard format that is easier to use
original_text_2_standardized = standardizetext(original_text_2, 1)

#Splits the string into words
original_text_2_words = original_text_2_standardized.split()

filter_input = getinput("Also, enter any words (separated by spaces) you would like the computer to filter out. Recommendations include \"and\", \"the\", \"is\", \"or\", \"a\", \"to\", \"of\", \"in\"", 0)

#Converts input to standard format that is easier to use
filter_input_standardized = standardizetext(filter_input, 0)

#Splits the string into words
outlawed_words = filter_input_standardized.split()

#declares the shared words list
shared_words = {}

#declares the first text's word position dictionary
original_text_1_word_position_dictionary = {}

#for loop that cycles through the first text and finds its position within the text, set based on the percent of the text that it is in, and stores it as a dictionary
i = 0
for word in original_text_1_words:
	percent_in_text = float(((i+1)/len(original_text_1_words))*100)
	original_text_1_word_position_dictionary[i] = {"position_percent":percent_in_text}
	i += 1

#declares the second text's word position dictionary
original_text_2_word_position_dictionary = {}

#for loop that cycles through the second text and finds its position within the text, set based on the percent of the text that it is in
i = 0
for word in original_text_2_words:
	percent_in_text = float(((i+1)/len(original_text_2_words))*100)
	original_text_2_word_position_dictionary[i] = {"position_percent":percent_in_text}
	i += 1

i = 0
i2 = 0

#goes through every single word in the first text
count_of_shared_words = 0
count_of_close_words = 0
for word in original_text_1_words:

	i2 = 0
	#Goes through each word in the second text per first word
	for second_word in original_text_2_words:
		#Finds out if the two words are the same
		if word == second_word:
			outlawed_word_alert = 0
			for outlawedword in outlawed_words:
				if word == outlawedword:
		  			outlawed_word_alert = 1

			#checks if it contains any of the filtered words. Skips if so
			if outlawed_word_alert == 0:
				#finds the difference between the two same words based on their position in the percentage throughout the text.
				difference = abs(original_text_1_word_position_dictionary[i]["position_percent"] - original_text_2_word_position_dictionary[i2]["position_percent"])		
				count_of_shared_words += 1
				
				#if the difference is less than or equal to 10, the program assumes the words are related and adds it to a counter of the close words
				if difference <= 10:
	  				count_of_close_words += 1
		i2 += 1

	i += 1

#formatting designed to improve user experience
print("")

print("--------------------------------------------------")

print("")

#if statement makes sure we do not divide by zero
if count_of_shared_words != 0:
	#finds how many words are considered to be related by the program
	percent_of_close_words = (float(count_of_close_words)/float(count_of_shared_words))*100
else:
	percent_of_close_words = 0

#prints output of the percentage
print("About "+str(int(percent_of_close_words))+"% of shared words are within the same region of the texts (error of 5%).")

#program provides simple analysis. if the percentage is greater than 30%, then the program presumes the texts are related, otherwise, not.
if percent_of_close_words > 30:
	print("The two texts are likely related.")
else:
  	print("The two texts are not likely related.")
