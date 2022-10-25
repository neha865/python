#pyPDF2 module
#pyttsx3

import PyPDF2
import pyttsx3
from pyttsx3 import Engine

Engine = pyttsx3.init()
PDF_Reader = PyPDF2.PdfFileReader(open("263.pdf", "rb"))
for Page_num in range(PDF_Reader.numPages):
    Text = PDF_Reader.getPage(Page_num).extractText()
    Engine.say(Text)
    Engine.runAndWait()
    #or use Engine.save_to_file(Text,"audio.mp3") for saving like an audio
