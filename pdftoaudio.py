# Install pyttsx3 and PyPDF2
#pip install pyttsx3
#pip install PyPDF2
import pyttsx3
import PyPDF2
from tkinter.filedialog import *
# Ask users where to open the pdf in their directories
book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
for x in range(0, pages):
    page= pdfreader.getPage(x)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

# Run the code!