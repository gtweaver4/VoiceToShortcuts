#
# recognize.py by Grant Weaver
#
# This class uses speech reconition and py audio to understand the users voice
#
import key
import speech_recognition as sr
import win32com.client

#creating list of possibler key combinations
#site with all the shortcuts: http://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html
def create_keylist():
	entry = ["ctrl","alt","bksp","down","up","left","right","enter","esc",
	"f1", "f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16",
	"shift","home", "ins", "help", "numlck", "pagedown", "pageup", "tab", "scrlock"]
	symbol = ["^","%","{BACKSPACE}","{DOWN}","{UP}","{LEFT}","{RIGHT}", "{ENTER}", "{ESC}",
	"{F1}","{F2}","{F3}","{F4}","{F5}","{F6}","{F7}","{F8}","{F9}","{F10}","{F11}","{F12}","{F13}","{F14}","{F15}","{F16}",
	"+","{HOME}", "{INSERT}", "{HELP}", "{NUMLOCK}", "{PGDN}", "{PGUP}", "{TAB}", "{SCROLLLOCK}"]
	keylist = []
	for x in range(0,len(entry)):
		shortcut_key = key.Key(entry[x], symbol[x])
		keylist.append(shortcut_key)

	return keylist


keylist = create_keylist()

#searches through the voice activators then finds the buttons to press
#if the activator is found
def recognize(word, activators, buttons):

	for x in range(0, len(activators)):
		if(activators[x] == word):
			print("Word is Recognized")
			shell = win32com.client.Dispatch("WScript.Shell")
			keypress = process_raw_button(buttons[x])
			print(keypress)
			shell.SendKeys(keypress)

#reads in the profile listens for audio then prints the word it
#thought you said
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
#site with all the shortcuts: http://win32com.goermezer.de/microsoft/windows/controlling-applications-via-sendkeys.html
def process_raw_button(buttons):
	processed_button = ""
	try:
		split = buttons.split("+")
	except:
		pass

	for x in range(0, len(split)):
		split[x] = split[x].strip()

	for x in range(0, len(split)):
		#search keylist for the keys
		for y in range(0, len(keylist)):
			if(split[x] == keylist[y].entry):
				split[x] = keylist[y].symbol

	for x in split:
		x = x.strip()
		processed_button = processed_button + x
	
	print(processed_button)
	return processed_button