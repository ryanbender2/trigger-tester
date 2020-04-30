import tkinter as tk
from tkinter import ttk
import pygubu
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from time import sleep
import csv
import pandas as pd

def on_Button_1_click():
    messagebox.showinfo('Getting Started', 'To get started, please load a CSV file into the empty space below by clicking the Load CSV button.')

def on_Button_2_click():
    filename = askopenfilename()
    
def on_Button_3_click():
    messagebox.showinfo('Create Report', 'Create Report') # placeholder message before correct code is implemented
    
def on_Button_4_click():
    messagebox.showinfo('Run', 'Run') # placeholder message before correct code is implemented
    
class CapstoneGUI:
    
    def __init__(self):

        self.builder = builder = pygubu.Builder()

        self.builder.add_from_file('Capstone_GUI\CapstoneGUI.ui')

        self.mainwindow = builder.get_object('MainFrame')
        
        callbacks = {
            'on_Button_1_clicked': on_Button_1_click,
            'on_Button_2_clicked': on_Button_2_click,
            'on_Button_3_clicked': on_Button_3_click,
            'on_Button_4_clicked': on_Button_4_click
        }
        
        builder.connect_callbacks(callbacks)
            
    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    CapstoneGUI().run()
