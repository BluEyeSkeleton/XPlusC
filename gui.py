# gui.py

import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.simpledialog import askinteger

from random import *
import webbrowser

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import integration as inte


# Use TkAgg in the backend of tkinter application
matplotlib.use("TkAgg")

class GUI(tk.Tk):
    """XPlusC GUI based on Tkinter"""
    def __init__(self, env, *args, **kwargs):
        """Initializes the GUI instance"""

        self.mainwindow_widgets = {}
        self.config = {
            "mode": inte.POWER_RULE,
            "use_coefficient": True, # False: Only easy questions without coefficients
            "fractional_coefficient": False, # False: only integers will be used for coefficients
            "max_integer": 6, # Maximum integer to be used as digit
            "min_integer": 2, # Minimum integer to be used as digit
        }

        self.__env = env

        super().__init__(*args, **kwargs)

    def init(self):
        pass

    def mainloop(self):
        # Perform first update
        self.__on_update()
        super().mainloop(0)

    # Called to generate new question and answer
    def __on_update(self, *_):
        self.config["mode"] = \
            self.vars["mode"].get() if self.vars["mode"].get() != 0 \
                else choice(inte.MODES)
        self.config["use_coefficient"] = self.vars["use_coefficient"].get()
        self.config["fractional_coefficient"] = \
            self.vars["fractional_coefficient"].get()
    
        (self.ques, self.ans) = inte.generate_definite_integral(self.config)
        self.show_question(self.ques)

    # Called to show answer
    def __on_show_answer(self):
        self.show_question_answer(self.ques, self.ans)

    # Set max integer
    def __set_max_integer(self):
        val = askinteger("Enter value", \
                            "Enter the maximum integer value " + \
                            "to be used as coefficient and power:", \
                            initialvalue=self.config["max_integer"])
        if (val == None):
            return
        if (val <= self.config["min_integer"]):
            showerror("Error",
                      "Maximum value must be larger than minimum value!")
            return
        self.config["max_integer"] = val

    # Set min integer
    def __set_min_integer(self):
        val = askinteger("Enter value", \
                            "Enter the minimum integer value " + \
                            "to be used as coefficient and power:", \
                            initialvalue=self.config["min_integer"])
        if (val == None):
            return
        if (val >= self.config["max_integer"]):
            showerror("Error",
                      "Minimum value must be smaller than maximum value!")
            return
        self.config["min_integer"] = val

    # Redirect user to GitHub page
    def __redir_github(self):
        webbrowser.open(self.__env["URL_GITHUB"], new=0, autoraise=True)

    # Redirect user to official website
    def __redir_website(self):
        webbrowser.open(self.__env["URL_WEBSITE"], new=0, autoraise=True)
  
    def render_mainwindow(self):
        w = self.mainwindow_widgets
        top = self.winfo_toplevel()

        # Variables
        self.vars = {
            "mode": IntVar(),
            "use_coefficient": BooleanVar(),
            "fractional_coefficient": BooleanVar(),
        }
        self.vars["mode"].set(0)
        self.vars["use_coefficient"].set(True)
        self.vars["fractional_coefficient"].set(False)

        # Configure GUI
        self.title("XPlusC: Master your basic integration skills")
        self.iconbitmap(default=self.__env["PATH_ICO"])
        self.geometry("960x360")
        self.resizable(False, False)

        # Add menu
        w["menu"] = Menu(top)
        top["menu"] = w["menu"]

        # Sub menu (Mode)
        w["menu_mode"] = Menu(w["menu"], tearoff=False)
        w["menu"].add_cascade(label="Mode", menu=w["menu_mode"])

        w["menu_mode"].add_radiobutton(
            label="Random", \
                variable=self.vars["mode"], value=0)
        w["menu_mode"].add_radiobutton(
            label="Power Rule (Basic)", \
                variable=self.vars["mode"], value=inte.POWER_RULE)
        w["menu_mode"].add_radiobutton(
            label="Power Rule (Linear)", \
                variable=self.vars["mode"], value=inte.POWER_RULE_LINEAR)
        w["menu_mode"].add_radiobutton(
            label="Power Rule (Basic with power of -1)", \
                variable=self.vars["mode"], value=inte.POWER_RULE_LN)
        w["menu_mode"].add_radiobutton(
            label="Power Rule (Linear with power of -1)", \
                variable=self.vars["mode"], value=inte.POWER_RULE_LN_LINEAR)
        w["menu_mode"].add_radiobutton(
            label="Exponent (Euler's number)", \
                variable=self.vars["mode"], value=inte.EXP_EULER)
        w["menu_mode"].add_radiobutton(
            label="Exponent (Integer)", \
                variable=self.vars["mode"], value=inte.EXP_INTEGER)
        w["menu_mode"].add_radiobutton(
            label="Trigonometry", \
                variable=self.vars["mode"], value=inte.TRIGO)
        w["menu_mode"].add_radiobutton(
            label="Trigonometry (Linear)", \
                variable=self.vars["mode"], value=inte.TRIGO_LINEAR)
        
        # Call update whenever the mode changes
        self.vars["mode"].trace_add("write", self.__on_update)
        
        # Sub menu (Options)
        w["menu_options"] = Menu(w["menu"], tearoff=False)
        w["menu"].add_cascade(label="Options", menu=w["menu_options"])

        w["menu_options"].add_checkbutton(
            label="Prepend numerical coefficient", \
                variable=self.vars["use_coefficient"])
        w["menu_options"].add_checkbutton(
            label="Include fractional coefficient", \
                variable=self.vars["fractional_coefficient"])
        w["menu_options"].add_command(
            label="Set maximum integer value for coefficient and power...", \
                command=self.__set_max_integer)
        w["menu_options"].add_command(
            label="Set minimum integer value for coefficient and power...", \
                command=self.__set_min_integer)
        
        # Sub menu (Help)
        w["menu_help"] = Menu(w["menu"], tearoff=False)
        w["menu"].add_cascade(label="Help", menu=w["menu_help"])

        w["menu_help"].add_command(
            label="Visit GitHub page for help...", \
                command=self.__redir_github)
        w["menu_help"].add_command(
            label="Visit Integration is Great! official website...", \
                command=self.__redir_website)

        # Add widgets
        w["desc"] = Label( \
            text="Evaluate the indefinite integral below " + \
            "and check your answer here:", \
                font=(self.__env["FONT_DEFAULT"], 16))
        w["footer"] = Label(text="© 2024 TeamX+C. All rights reserved.",
                          font=(self.__env["FONT_DEFAULT"], 8))
        w["canvas_master"] = Label()
        w["btn_shuffle"] = Button(text="Shuffle",
                                  font=(self.__env["FONT_DEFAULT"], 24),
                                  command=self.__on_update)
        w["btn_answer"] = Button(text="Show Answer",
                                  font=(self.__env["FONT_DEFAULT"], 24),
                                  command=self.__on_show_answer)        

        # Define the figure size and plot the figure
        fig = matplotlib.figure.Figure(figsize=(10, 2), dpi=100)
        self.wx = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=w["canvas_master"])
        self.canvas.get_tk_widget().pack(side=TOP, fill=X, expand=0)
        self.canvas._tkcanvas.pack(side=TOP, fill=X, expand=0)

        # Set the visibility of the Canvas figure
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)

        # Place widgets
        w["desc"].place(anchor=N, relx=0.5, rely=0.01)
        w["footer"].place(anchor=SW, relx=0.01, rely=0.99)
        w["canvas_master"].place(anchor=N, relx=0.5, rely=0.1)
        w["btn_shuffle"].place(anchor=W, relx=0.1, rely=0.82)
        w["btn_answer"].place(anchor=E, relx=0.9, rely=0.82)
        
    def show_question(self, tex):
        # Clear any previous Syntax from the figure
        self.wx.clear()
        self.wx.text(0.1, 0.5, f"${tex}$", fontsize = 24)
        self.canvas.draw()

    def show_question_answer(self, tex_ques, tex_ans):
        # Clear any previous Syntax from the figure
        self.wx.clear()
        self.wx.text(0.1, 0.5, f"${tex_ques} = {tex_ans}$", fontsize = 24)
        self.canvas.draw()