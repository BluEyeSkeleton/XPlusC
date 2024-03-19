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
w = window.widgets
top = window.winfo_toplevel()

# Configure GUI
window.title("XPlusC: Master your integration skills")
window.iconphoto(True, PhotoImage(file="img/favicon.png"))
window.geometry("640x480")
window.resizable(False, False)

# Menu bar
window.addMenu("menu", top)
top["menu"] = w["menu"]

# Sub menu
window.addMenu("menu_home", w["menu"])
w["menu"].add_cascade(label="Home", menu=w["menu_home"])

# Add widgets
window.addLabel("title", text="XPlusC", font=(environ["FONT_DEFAULT"], 24))
window.addLabel("desc", text="© 2024 TeamX+C. All rights reserved.", font=(environ["FONT_DEFAULT"], 8))

w["title"].place(anchor=N, relx=0.5, rely=0.01)
w["desc"].place(anchor=SW, relx=0.01, rely=0.99)

# Test
#inte = DefiniteIntegral("", 2, 3)

# Loop it
window.mainloop()