# Aaron Martin
# Natural Language Programming Assignment 1
# Eliza the Academic Advisor
#
# Chatbot that takes in input and uses regular expressions through the re library
# to match that text with a list of rules and a response is chosen that may use
# information from the capture groups

import random
import re

pronounDict = {
	"i": "you",
	"you": "me",
	"me": "you",
	"am": "are",
	"my": "your",
	"your": "my",
	"yours": "mine",
	"are": "am"
}

rules = [

[r"(.*)(\bhello\b|\bhi\b)(.*)", ["Hello, I am an academic advisor, what is your name?", "Hey, whats your name?", "Hello, My name is eliza, whats your name?"]],
[r"(.*)shit(.*)", ["Hey now, no need to curse!", "Bro, stop swearing."]],
[r"(.*)homework(.*)", ["Homework is critical. Have the classes you've been taking had a lot?"]],

[r"(my name is)? ([A-Z][a-z]*$)", ["Hello {1}! What is your Major?", "Nice to meet you {1}, what can I help you with?", "Hi {1}, what degree are you seeking?"]], 

[r"i( am in|'?m in| am studying|'?m studying) (.*)", ["What classes have you taken so far for {1}?", "Do you like being in {1}?", "That seems like a very good choice", "How many people do you know are taking {1}?"]], 

[r"(\b.*\b)* \band\b \b.*\b", ["Have you been doing well with those?"]],

[r"\bi\b (\blike\b|\blove\b|\bhate\b|\bdespise\b) (.*)", ["Why do you {} {}"]],

[r"i(.*)(\bdoing\b|is going)?(\bgood\b|\bwell\b|\bok\b|\bbad\b|\bterrible\b)", ["What makes it go {2}?"]],

[r"i don'?t know (.*)", ["Where do you think you could find {}?"]],

[r"(.*)(\bwant\b|\bneed\b) to take (\b[a-z]*\b)(.*)", ["Are you excited for {2}?", "Do you need {2} for another class?"]],

[r"(.*)have(n'?t| not) (.*)", ["Why have you not {2}?", "Do you need to {2}?"]],

[r"(.*)feeling(.*)about(.*)", ["What makes you feel {1} about {2}"]],

[r"(.*)\b[a-z]*\b(.*)yours?( name)?\?", ["My name is Eliza."]],

[r"(.*) is fun", ["What makes {} fun?"]],

[r"(.*)(good)? grades?(.*)", ["Those grades are important when considering what classes you will need to take for the future", "You will need those at least C- grades for prerequisites"]],

[r"(.*)graduate(.*)(\bon\b|\bin\b) time(.*)", ["Graduating is important, but make sure you aren't over working yourself.", "Would taking extra years be detrimental to your learning experience?"]],

[r"(.*)(\bcredit\b|\bgpa\b)(.*)\?", ["Have you looked at your APAS to find out more about {1}?"]],

[r"(.*)", [
"How do you think you are doing in your classes?",
"What classes would you like to take?",
"When do you plan to graduate?",
"have you looked into other classes to help with your eventual career?",
"How are you feeling about this semester?",
"Do you think you are going to graduate on time?",
"Interesting", "Please expand on that", "Tell me more"]]

]

memory = []

#Swapping pronouns
def swapPronouns(raw):
	if raw is not None:
		#split text from captured group into individual words
		group = raw.split()
		newGroup = []
	
		#Iterate each word in group
		for t in group:
			#Iterate the dictionary, and swap as necessary
			for old in pronounDict:
				if t == old:
					t = pronounDict[old]
					break;
			newGroup.append(t)
		return (" ").join(newGroup)
	else:
		return raw

#Parse the input
def parse(text):
	#Iterate over all of the rules
	for rule, value in rules:

		#Check if regex match found on input
		match = re.match(rule, text, re.I)
		if match is not None:
			#random.choice() -> Choose from list of responses based on match
			#.format() -> associate each capture group with sections of response string
			#swapPronouns(group) for group in match.groups() -> Iterate through each capture group in the match, passing each one into the pronoun swapping function
			output = random.choice(value).format(*[swapPronouns(group) for group in match.groups()])
			break;
		else:
			output = "Failure"
	return output

			

while(True):
	text = input("> ").lower().rsplit(".")[0]

	print(parse(text))
