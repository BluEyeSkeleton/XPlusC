# Imports
#from os import environ
#from dotenv import load_dotenv

from gui import GUI

# Load environment variables
#load_dotenv()
environ = {
    "FONT_DEFAULT": "Times New Roman",
    "PATH_ICO": "img/icon.ico",
    "URL_GITHUB": "https://github.com/BluEyeSkeleton/XPlusC",
    "URL_WEBSITE": "https://integration.is-great.org/",
}

# Initialize GUI instance
window = GUI(env=environ)
window.render_mainwindow()

# Loop it
window.mainloop()