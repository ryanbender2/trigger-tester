"""Capstone_GUI.py -- Contains the class for interface."""

import tkinter as tk
from tkinter import ttk
import pygubu
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from time import sleep
import csv
import pandas as pd
from DataSetCleanse import DataSetCleanse
from ntpath import basename
from os import getcwd


class CapstoneGUI(object):
    """Interface for Financial Data Processor (FDP)."""
    
    def __init__(self):
        """Init class."""
        # init interface
        self.builder = builder = pygubu.Builder()
        self.builder.add_from_file('Capstone_GUI\CapstoneGUI.ui')
        self.mainwindow = builder.get_object('MainFrame')
        
        # dataset
        self.filepath = None
        self.dataset = None
        
        # button assignments
        callbacks = {
            'on_Button_1_clicked': self.on_Button_1_click,
            'on_Button_2_clicked': self.on_Button_2_click,
            'on_Button_3_clicked': self.on_Button_3_click,
            'on_Button_4_clicked': self.on_Button_4_click
        }
        self.output_box = builder.get_object('Output_Box')
        self.undefined_callbacks = builder.connect_callbacks(callbacks)
        
        self.output_box.insert("end", "")
        
    def _write_to_output(self, output):
        self.output_box.insert("end", output)
        
    def _clear_output(self):
        self.output_box.delete("1.0", "end")
    
    def on_Button_1_click(self):
        messagebox.showinfo('Getting Started', 'To get started, please load a CSV file into the empty space below by clicking the Load CSV button.')
        
    def on_Button_2_click(self):
        self.filepath = askopenfilename()
        # self.dataset = DataSetCleanse(self.filepath)
        
        # to_output = "Loaded file: {}\n{}\n\n".format(basename(self.filepath), self.dataset.describe())
        # top = ''
        # for row in self.dataset.getDataSet()[:5]: top += ', '.join(row) + '\n'
        # to_output += top
        # self._write_to_output(to_output)
        self._write_to_output('hello')

        
    def on_Button_3_click(self):
        messagebox.showinfo('Create Report', 'Create Report') # placeholder message before correct code is implemented
        
    def on_Button_4_click(self):
        messagebox.showinfo('Run', 'Run') # placeholder message before correct code is implemented
            
    def run(self):
        """Start app."""
        self.mainwindow.mainloop()

if __name__ == '__main__':
    CapstoneGUI().run()
