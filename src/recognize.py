#
# recognize.py by Grant Weaver
#
# This class uses speech reconition and py audio to understand the users voice
#

import speech_recognition as sr

def recognize():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		print("You said " + r.recognize_google(audio))    
	except:                           
		print("Could not understand audio")