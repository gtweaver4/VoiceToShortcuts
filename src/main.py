#
# main.py by Grant Weaver
#
# This class will contain the gui for the interface

import recognize
from Tkinter import *
import sys
import os
import shutil
import glob

#creating main window
root = Tk()
root.title('Select preferences')
root.geometry('600x600')
current_profile = StringVar("")
current_profile.set("Profile: ")

#this starts the program
def start():
	recognize.recognize()

#this reads in the current profiles of the users
#for the main window to be able to display them
#returns an array of profiles
def read_in_profiles():
	profiles = []
	default_dir = get_default_profile_dir()
	user_dir = get_user_profile_dir()
	files = os.listdir(default_dir)
	for f in files:
		profiles.append(f)
	files = os.listdir(user_dir)
	for f in files:
		profiles.append(f)
	return profiles

#sets the current profile for the user
def set_profile(name):
	current_profile.set("Profile: " + name)

#saves the profile the user creates into the userdat folder
def save(name, voiceArr, buttonArr):
	file_name = name + ".dat"
	try:
		#if emptyname raise exception
		if(name == ""):
			raise FileNameError('blank file name')

		#attempt to create .dat file and write information to it
		f = open(file_name, "w+")
		for x in range(0, len(voiceArr)):
			f.write("voiceactivator:" + voiceArr[x] + "\tbuttonqueued:" + buttonArr[x] + "\n")

	except:
		Label(create, text = "\nPlease enter a valid name.").pack()

	f.close()
	#moves files after saving the files
	move_files()

#moves .dat files from the src folder to the userdat dir
def move_files():
	try:
		source_folder = os.getcwd()
		destination_folder = get_user_profile_dir()
	except:
		print("error finding source folder")

	files = os.listdir(source_folder)
	for f in files:
		if(f.endswith(".dat")):
			shutil.move(f, destination_folder)

	raise_frame(home)
		
#gets the user profile dir as string
def get_user_profile_dir():
	try:
		source_folder = os.getcwd()
		sf_split = source_folder.split("\\")
		destination_folder = ""
		for x in range(0, len(sf_split) - 1):
			destination_folder = destination_folder + sf_split[x] + "\\"
		destination_folder = destination_folder + "profiledat\\userdat\\"
		return destination_folder
	except:
		print("error finding source folder")

#gets the default profile dir as a string
def get_default_profile_dir():
	try:
		source_folder = os.getcwd()
		sf_split = source_folder.split("\\")
		destination_folder = ""
		for x in range(0, len(sf_split) - 1):
			destination_folder = destination_folder + sf_split[x] + "\\"
		destination_folder = destination_folder + "profiledat\\defaultdat\\"
		return destination_folder
	except:
		print("error finding source folder")

#adds the voice and buttons to the array so they can be saved
#also creates a label showing a label with the button and voice activation
def add_entry(voice, button, voiceArr,buttonArr):
	voiceArr.append(voice.get())
	buttonArr.append(button.get())
	Label(create, text = ("Voice Shortcut: " + voice.get() + "Buttons Pressed: " + button.get())).pack()

#this changes the frames
def raise_frame(frame):
    frame.tkraise()

#setting default frames
home = Frame(root)
edit = Frame(root)
create = Frame(root)

#setups up frames so they dont overlap
for frame in (home, edit, create):
    frame.grid(row=0, column=0, sticky='news')



#######################
#######################
#HOME SCREEEN
home_profile_label = Label(home, textvariable = current_profile)
home_profile_label.pack() #on seperate lines to allow the label to update
Button(home, text='Edit Profiles', command=lambda:raise_frame(edit)).pack()
Button(home, text='Create New Profile', command=lambda:raise_frame(create)).pack()
Button(home, text='Start Voice Shortcuts', command=lambda:start()).pack()
Button(home, text='Cancel', command=lambda:sys.exit()).pack()



#######################
#######################
#EDIT PROFILES
profile_list = read_in_profiles()
Label(edit, text='Edit').pack()
edit_profile_label = Label(edit, textvariable = current_profile)
edit_profile_label.pack() #on seperate lines to allow the label to update
for x in profile_list:
	Button(edit, text = x, command = lambda:set_profile(x)).pack()
Button(edit, text='Home', command=lambda:raise_frame(home)).pack()
Button(edit, text='Cancel', command=lambda:sys.exit()).pack()




#######################
#######################
#CREATE PROFILES
Label(create, text='Create Profile').pack()

#createFrame1 is for the horizontal allignment of widgets
createFrame1 = Frame(create)
Label(createFrame1, text = "Name of Profile: ").pack(side='left')

#profile name frame
profile_name = StringVar()
profile_name_entry = Entry(createFrame1, textvariable = profile_name)
profile_name_entry.pack(side = 'left')
createFrame1.pack()

#frame for the entry widgets
createFrame2 = Frame(create)
voice = StringVar()
button = StringVar()
voiceArr = []
buttonArr = []
Label(createFrame2, text = "Voice Shortcut: ").pack(side = 'left')
Entry(createFrame2, textvariable = voice).pack(side='left')
Label(createFrame2, text = "\tButton Combination: ").pack(side='left')
Entry(createFrame2, textvariable = button).pack(side='left')
createFrame2.pack()
Button(create, text = "add", command = lambda:add_entry(voice, button, voiceArr,buttonArr)).pack()

#frame for buttons
buttonFrame = Frame(create)
Button(buttonFrame, text='Home', command=lambda:raise_frame(home)).pack(side='left')
Button(buttonFrame, text='Save', command=lambda:save(profile_name.get(), voiceArr, buttonArr)).pack(side='left')
Button(buttonFrame, text='Cancel', command=lambda:sys.exit()).pack(side='left')
buttonFrame.pack()

#setting default frame and starting mainloop
raise_frame(home)
root.mainloop()