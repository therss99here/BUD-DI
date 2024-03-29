# Import the required module for text
# to speech conversion 
from gtts import gTTS


# Text that will be converted to audio
mytext = "Hi, I am your friendly, neighbour hood Assistant, Buddy!"

# Language in which you want to convert, generally its english
language = 'en'

# Passing the text and language to the engine, here we have marked slow=False. Which tells  the module that the converted audio should  have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named welcome
myobj.save("welcome.mp3")

