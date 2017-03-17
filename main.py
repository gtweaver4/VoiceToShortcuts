#
# main.py by Grant Weaver
#
# This class will contain the gui for the interface

import recognize
from Tkinter import *
import sys

#creating main window
root = Tk()
root.title('Select preferences')
root.geometry('400x500')
current_profile = StringVar("")
current_profile.set("Profile: ")

#this starts the program
def start():
	i=0

#this reads in the current profiles of the users
#for the main window to be able to display them
#returns an array of profiles
def read_in_profiles():
	i=0

#sets the current profile for the user
def set_profile(name):
	current_profile.set("Profile: " + name)

#this changes the frames
def raise_frame(frame):
    frame.tkraise()

home = Frame(root)
edit = Frame(root)
create = Frame(root)

#setups up frames so they dont overlap
for frame in (home, edit, create):
    frame.grid(row=0, column=0, sticky='news')

#######################
#HOME SCREEEN
home_profile_label = Label(home, textvariable = current_profile)
home_profile_label.pack() #on seperate lines to allow the label to update
Button(home, text='Edit Profiles', command=lambda:raise_frame(edit)).pack()
Button(home, text='Create New Profile', command=lambda:raise_frame(create)).pack()
Button(home, text='Start Voice Shortcuts', command=lambda:start()).pack()
Button(home, text='Cancel', command=lambda:sys.exit()).pack()

#######################
#EDIT PROFILES
test = ['one', 'two', 'three', 'four']
Label(edit, text='Edit').pack()
edit_profile_label = Label(edit, textvariable = current_profile)
edit_profile_label.pack() #on seperate lines to allow the label to update
for x in range(0, len(test)):
	b = Button(edit, text = test[x], command = lambda:set_profile(b['text'])).pack()
Button(edit, text='Home', command=lambda:raise_frame(home)).pack()
Button(edit, text='Cancel', command=lambda:sys.exit()).pack()

#######################
#CREATE PROFILES
Label(create, text='Create Profile').pack()

#createFrame1 is for the horizontal allignment of widgets
createFrame1 = Frame(root)
Label(createFrame1, text = "Name of Profile: ").pack(side='left')
profile_name = StringVar()
profile_name_entry = Entry(create, textvariable = profile_name)
profile_name_entry.pack(side = 'left')
createFrame1.pack()

Button(create, text='Cancel', command=lambda:sys.exit()).pack()



raise_frame(home)
root.mainloop()






#start the tk window
while(True):
	root.mainloop()