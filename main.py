# Imports
from os import environ
from dotenv import load_dotenv

from gui import GUI

import integration as inte

# Load environment variables
load_dotenv()

# Initialize GUI instance
window = GUI(env=environ)

# Test
CONFIG = {
    "mode": inte.EXP_EULER,
    "use_coefficient": True, # False: Only easy questions without coefficients
    "fractional_coefficient": False, # False: only integers will be used for coefficients
    "max_integer": 6, # Maximum integer to be used as digit
    "min_integer": 2, # Minimum integer to be used as digit
}
(ques, ans) = inte.generate_definite_integral(CONFIG)
window.show_question_answer(ques, ans)

# Loop it
window.mainloop()