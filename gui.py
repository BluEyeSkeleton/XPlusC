# gui.py

import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import integration as inte

import sympy

# Use TkAgg in the backend of tkinter application
matplotlib.use('TkAgg')

class GUI(tk.Tk):
    """GUI based on Tkinter"""
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
        self.render_mainwindow()

    def init(self):
        pass
  
    def render_mainwindow(self):
        w = self.mainwindow_widgets
        top = self.winfo_toplevel()

        self.vars = {
            "mode": IntVar(),
            "use_coefficient": BooleanVar(),
            "fractional_coefficient": BooleanVar(),
        }
        def __mode(*args):
            self.config["mode"] = self.vars["mode"].get()
            print(self.config["mode"])
        self.vars["mode"].trace_add("write", __mode)

        # Configure GUI
        self.title("XPlusC: Master your integration skills")
        self.iconphoto(True, PhotoImage(file="img/favicon.png"))
        self.geometry("640x480")
        self.resizable(False, False)

        # Add menu
        w["menu"] = Menu(top)
        top["menu"] = w["menu"]

        # Sub menu
        w["menu_mode"] = Menu(w["menu"], tearoff=False)
        w["menu"].add_cascade(label="Mode", menu=w["menu_mode"])

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

        # Add widgets
        w["title"] = Label(text="XPlusC",
                           font=(self.__env["FONT_DEFAULT"], 24))
        w["desc"] = Label(text="© 2024 TeamX+C. All rights reserved.",
                          font=(self.__env["FONT_DEFAULT"], 8))
        w["canvas_master"] = Label()

        # Define the figure size and plot the figure
        fig = matplotlib.figure.Figure(figsize=(7, 2), dpi=100)
        self.wx = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=w["canvas_master"])
        self.canvas.get_tk_widget().pack(side=TOP, fill=X, expand=0)
        self.canvas._tkcanvas.pack(side=TOP, fill=X, expand=0)

        # Set the visibility of the Canvas figure
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)

        # Place widgets
        w["title"].place(anchor=N, relx=0.5, rely=0.01)
        w["desc"].place(anchor=SW, relx=0.01, rely=0.99)
        w["canvas_master"].place(anchor=N, relx=0.5, rely=0.1)
        
    def show_question(self, tex):
        # Clear any previous Syntax from the figure
        self.wx.clear()
        self.wx.text(0.2, 0.2, f"${tex}$", fontsize = 24)
        self.canvas.draw()

    def show_question_answer(self, tex_ques, tex_ans):
        # Clear any previous Syntax from the figure
        self.wx.clear()
        self.wx.text(0.1, 0.75, f"${tex_ques} = {tex_ans}$", fontsize = 24, va="top", ha="left")
        self.canvas.draw()