
# Name:                 gTTS (Google Text to-speech)
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version               1.0
# Created               30/07/2024
# Copyright             (c) Muzaffar Ali
# License               Public
# Requirements-1:       gTTS (Google Text-to-Speech): This is a module and class that interfaces with Google's Text-to-Speech API. It converts text into spoken audio.
# Requirements-1:       os: This module provides a way to use operating system-dependent functionality like reading or writing to the file system.


from gtts import gTTS
import os

# Open the file "intro.txt" in read mode and read its contents
file = open("intro.txt", "r").read()

# Create a gTTS object with the text from the file
# lang="en" specifies the language as English
# slow=False specifies that the speech should be at normal speed
speech = gTTS(text=file, lang="en", slow=False)

# Save the speech audio to a file named "ali.mp3"
speech.save("ali.mp3")

# Play the saved MP3 file
os.system("ali.mp3")

# Print the contents of the file to the console
print(file)
