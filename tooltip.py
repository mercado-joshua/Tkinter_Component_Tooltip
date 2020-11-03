#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd

class Create_ToolTip:
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        if self.tip_window or not tip_text:
            return

        x, y, _cx, cy = self.widget.bbox('insert')      # get size of widget
        x = x + self.widget.winfo_rootx() + 25          # calculate to display tooltip
        y = y + cy + self.widget.winfo_rooty() + 25     # below and to the right

        self.tip_window = tw = tk.Toplevel(self.widget) # create new tooltip window
        tw.wm_overrideredirect(True)                    # remove all Window Manager (wm) decorations
        tw.wm_geometry(f'+{x}+{y}')                     # create window size

        label = tk.Label(
            tw,
            text=tip_text,
            justify=tk.LEFT,
            background='#ffffe0',
            relief=tk.SOLID,
            borderwidth=1,
            font=('sans-serif', '10', 'normal'))
        label.pack(ipadx=10, ipady=5)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

#===========================
# Main Component
#===========================

class ToolTip:
    """Display text in a tooltip window."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = Create_ToolTip(self.widget)
        self.init_events()

    def init_events(self):
        self.widget.bind('<Enter>', self.enter)   # bind mouse events
        self.widget.bind('<Leave>', self.leave)

    def enter(self, event):
        self.tooltip.show_tip(self.text)

    def leave(self, event):
        self.tooltip.hide_tip()