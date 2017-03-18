#
# recognize.py by Grant Weaver
#
# This class uses speech reconition and py audio to understand the users voice
#

import speech_recognition as sr
import win32com.client

def recognize(word):
	activators = import_activators()
	buttons = import_buttons()

	for x in range(0, len(activators)):
		if(activators[x] == word):
			shell = win32com.client.Dispatch("WScript.Shell")
			keypress = process_raw_button(buttons[x])
			shell.SendKeys(keypress)

def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		word = r.recognize_google(audio)
		print(word)
	except:                           
		print("Could not understand audio")

	recognize(word)

def import_activators():
	return ["save","exit","underline"]

def import_buttons():
	return ["ctrl + s", "alt + f4", "ctrl + u"]

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