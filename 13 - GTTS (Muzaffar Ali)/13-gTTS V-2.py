

# Name:                 gTTS (Google Text to-speech)
# Purpose:              Advance Python Class
# Author:               Muzaffar Ali
# Version               1.0
# Created               30/07/2024
# Copyright             (c) Muzaffar Ali
# License               Public
# Requirements-1:       gTTS (Google Text-to-Speech): This is a module and class that interfaces with Google's Text-to-Speech API. It converts text into spoken audio.


# Import the gTTS (Google Text-to-Speech) class from the gtts module
from gtts import gTTS

# Prompt the user to input their message and store it in the variable 'message'
message = input("Please input your message: ")

# Create a gTTS object with the user-provided text
tts = gTTS(message)

# Save the speech audio to a file named "intro.mp3"
tts.save("intro.mp3")
