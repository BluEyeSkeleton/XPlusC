# GUI
# Utility class for Python Tkinter UI.

import tkinter as tk

class GUI(tk.Tk):
  """GUI based on Tkinter"""
  def __init__(self, *args, **kwargs):
    """Initializes the GUI instance"""
    self.WIDGET_NAMES = [ # All widgets available in tk
      "Button",
      "Checkbutton",
      "Entry",
      "Frame",
      "Label",
      "LabelFrame",
      "Menubutton",
      "PanedWindow",
      "Radiobutton",
      "Scale",
      "Scrollbar",
      "Spinbox"
    ]
    self.widgets = {}
    for widgetName in self.WIDGET_NAMES:
      # Dynamically declare methods to add widgets
      self.createAddWidgetMethod(widgetName)
    super().__init__(*args, **kwargs)

  def init(self):
    pass

  def createAddWidgetMethod(self, widgetName):
    def method(widgetId, **kwargs):
      self.widgets[widgetId] = eval(f"tk.{widgetName}(**kwargs)", globals(), locals())
      return self.widgets[widgetId]
    setattr(self, f"add{widgetName}", method)