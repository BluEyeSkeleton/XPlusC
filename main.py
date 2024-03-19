# Imports
from os import environ
from dotenv import load_dotenv

from gui import GUI
from tkinter import *

from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

from integral import DefiniteIntegral

# Load environment variables
load_dotenv()

# Initialize GUI instance
window = GUI()
widgets = window.widgets

# Configure GUI
window.title("XPlusC: Master your integration skills")
window.iconphoto(True, PhotoImage(file="img/favicon.png"))
window.geometry("640x480")
window.resizable(False, False)

# Add widgets
window.addLabel("title", text="XPlusC", font=(environ["FONT_DEFAULT"], 24))
window.addLabel("desc", text="© 2024 TeamX+C. All rights reserved.", font=(environ["FONT_DEFAULT"], 8))


widgets["title"].place(anchor=N, relx=0.5, rely=0.01)
widgets["desc"].place(anchor=SW, relx=0.01, rely=0.99)

#Test
inte = DefiniteIntegral("(x+4)*(x-2)**8", 2, 3)
print(inte.evaluate())

# Loop it
window.mainloop()