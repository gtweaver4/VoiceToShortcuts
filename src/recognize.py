#
# recognize.py by Grant Weaver
#
# This class uses speech reconition and py audio to understand the users voice
#

import speech_recognition as sr
import win32com.client

def recognize(word, activators, buttons):

	for x in range(0, len(activators)):
		if(activators[x] == word):
			print("True")
			print(activators[x][0])
			print(buttons[x][0])
			shell = win32com.client.Dispatch("WScript.Shell")
			keypress = process_raw_button(buttons[x])
			shell.SendKeys(keypress)

def listen(file):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	#try read in the profile
	try:
		f = open(file, "r")
		activators = []
		buttons = []
		keyword = "&"
		for line in f: #goes line by line and splits lines by keyword
			voice,keyword,button = line.partition(keyword)
			activators.append(voice)
			buttons.append(button)
		f.close()
	except:
		print("could not find profile")

	#try recognizing the word
	try:
		word = r.recognize_google(audio)
		print(word)
		print(activators)
		print(buttons)
		recognize(word, activators, buttons)
	except:                           
		print("Could not understand audio")


#processes buttons and turns things like control into ^
def process_raw_button(buttons):
	processed_button = ""
	try:
		split = buttons.split("+")
	except:
		pass

	for x in range(0, len(split)):
		split[x] = split[x].strip()

	for x in range(0, len(split)):
		if(split[x] == "ctrl"):
			split[x] = "^"

	for x in split:
		x = x.strip()
		processed_button = processed_button + x
	
	print(processed_button)
	return processed_button