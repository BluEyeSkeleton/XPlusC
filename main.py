# Imports
from os import environ
from dotenv import load_dotenv

from gui import GUI
from random import *

import integration as inte

# Load environment variables
load_dotenv()
ques = None
ans = None

# Initialize GUI instance
window = GUI(env=environ)

# On update
def on_update():
    global ques, ans, window
    window.config["mode"] = \
        window.vars["mode"].get() if window.vars["mode"].get() != 0 \
            else choice(inte.MODES)
    
    (ques, ans) = inte.generate_definite_integral(window.config)
    window.show_question(ques)
def on_show_answer():
    global ques, ans, window
    window.show_question_answer(ques, ans)
window.set_handlers(on_update, on_show_answer)

# Loop it
window.mainloop()