"""Capstone_GUI.py -- Contains the class for interface."""

import tkinter as tk
from tkinter import ttk
import pygubu
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import csv
import pandas as pd
from pandas import read_csv
from DataSetCleanse import DataSetCleanse
from ntpath import basename
from os import getcwd

from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


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
        self.run_results = None
        self.selected_alg = None
        
        # button assignments
        callbacks = {
            'on_Button_1_clicked': self.on_Button_1_click,
            'on_Button_2_clicked': self.on_Button_2_click,
            'on_Button_4_clicked': self.on_Button_4_click
        }
        self.output_box = builder.get_object('Output_Box')
        self.alg_options = builder.get_object('Algorithm_Choice')
        
        options = ['SVM', 'Logistic Regression']
        self.alg_options.config(values=options)
        self.alg_options.bind('<<ComboboxSelected>>', self.on_alg_select)
        
        self.undefined_callbacks = builder.connect_callbacks(callbacks)

        self.output_box.insert("end", "")
    
    def on_alg_select(self, event):
        self.selected_alg = str(self.alg_options.get())
        
    def _write_to_output(self, output):
        self.output_box.insert("end", '\n' * 2)
        self.output_box.insert("end", str(output))

    def on_Button_1_click(self):
        messagebox.showinfo('Getting Started', 'To get started, Select an algorithm to use and load data.')
        
    def on_Button_2_click(self):
        self.filepath = askopenfilename()
        self.dataset = DataSetCleanse(self.filepath)
        
        to_output = "Loaded file: {}\n{}\n\n".format(basename(self.filepath), self.dataset.describe())
        top = ''
        for row in self.dataset.getDataSet()[:5]: top += ', '.join(row) + '\n'
        to_output += top
        self.output_box.insert("end", to_output)
        
    def on_Button_4_click(self):
        """Run algorithm."""
        algorithm = self.selected_alg
        filepath = self.filepath
        
        if not self.dataset:
            self._write_to_output('Please load data.')
            return
    
        names = self.dataset.getTitles()
        dataset = read_csv(filepath, names=names)
        
        if not self.dataset:
            self._write_to_output('Please load data.')
            return
        
        if not algorithm:
            self._write_to_output('Please select algorithm first.')
            return

        # Split-out validation dataset
        array = dataset.values[1:]
        X = array[:, 0:1]
        y = array[:, 1]
        X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

        # Make predictions on validation dataset
        if algorithm == 'SVM':
            model = SVC()
        if algorithm == 'Logistic Regression':
            model = LogisticRegression()

        model.fit(X_train, Y_train)
        predictions = model.predict(X_validation)
        results = classification_report(Y_validation, predictions, digits=7)
        self._write_to_output('Algorithm %s' % algorithm)
        self._write_to_output(results)
            
    def run(self):
        """Start app."""
        self.mainwindow.mainloop()


if __name__ == '__main__':
    CapstoneGUI().run()
