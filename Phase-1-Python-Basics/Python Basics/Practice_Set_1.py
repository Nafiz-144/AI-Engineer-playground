# problem-1
print('''“And [mention] the man of the fish, when he went off in anger and thought that We would not decree [anything] upon him. And he called out within the darknesses, “There is no deity except You; exalted, are You. Indeed, I have been of the wrongdoers.” it continues on, “So We responded to him and saved him from the distress. And thus do We save the believers.”
If you’re familiar with the story of Prophet Yunus you’ll know that Prophet Yunus gave up on his people. Without the permission of Allah, he decided to leave the city of Nineveh in hopes to find a city that would more readily accept him and the message of Islam. This is why the Quran mentions “the man of the fish, when he went off in anger and thought that We would not decree [anything] upon him”.
As punishment he was kicked off and abandoned by his ship members, swallowed by a whale, and left in darkness. At this moment he cried out remembering Allah, praising Allah, admitting his faults in the matter by saying “Indeed, I have been of the wrongdoers.”
Allah seeing the genuine and sincere apology had then relieve him.
      ''')
# problem-2
#REPL The Python REPL (Read-Eval-Print Loop) is an interactive shell for executing Python code line-by-line and receiving immediate feedback.
# problem-3
import pyttsx3
engine = pyttsx3.init()
engine.say("La ilaha illa anta subhanaka inni kuntu minaz zalimin")
engine.runAndWait()
# Single line usage with speak function with default options
import pyttsx3
pyttsx3.speak("Single line usage with speak function with default options")

# Changing Voice , Rate and Volume 
import pyttsx3
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

engine.say("Hello Nafiz You can do it")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file('Hello Nafiz You can do it', 'test.mp3')
engine.runAndWait()

#problem-4
# Author: Sadman
# Location: Earth
# Date: 2026-03-30

import os

directory_path = '.'  # current folder

try:
    contents = os.listdir(directory_path)
    for item in contents:
        print(item)
except Exception as e:
    print("Error:", e)

# import os

# # Select the directory whose content you want to list
# # Use '.' to refer to the current directory
# directory_path = '/' 

# # Use the os.listdir() function to get a list of all files and folders
# contents = os.listdir(directory_path)

# # Print the list of contents
# print(contents)