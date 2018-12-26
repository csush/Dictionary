import json

# to generate closeness of words for user suggestions
import difflib
from difflib import get_close_matches

#loading json data as python dictionary
data = json.load(open("dictionary.json"))

#Function to retrieve definition from json dictionary
def retrieve_definition(word):
	#Removing case sensitivity
	word = word.lower()

	#Check for non-existing words
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		action = input(("Did you mean %s instead? [y/n]: " % get_close_matches(word, data.keys())[0]))
		if (action == "y"):
			return data[get_close_matches(word, data.keys())[0]]
		elif (action == "n"):
			return ("Word doesn't exist :(")
		else: return ("Invalid input :/")

word_user = input("Enter a word: ")

output = retrieve_definition(word_user)

if type(output) == list:
	for item in output:
		print("-", item)
else: print("-", output)