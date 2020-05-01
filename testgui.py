
try:
    import tkinter as tk
except:
    import Tkinter as tk
import sys
import os
import re
import glob
import pygubu
#
#
DATA_DIR = os.path.abspath(os.path.dirname(__file__))
if getattr(sys, 'frozen', False):
    DATA_DIR = os.path.abspath(os.path.dirname(sys.executable))
directory = glob.glob('**', recursive=True)


class Application:
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()
        
        #2: Load an ui file
        builder.add_from_file(os.path.join(DATA_DIR, 'testui_ui'))
        # builder.add_resource_path(os.path.join(DATA_DIR, 'imgs'))
        #
        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow')
        self.SearchStringVAR = builder.get_variable('SearchString')
        self.SourceFolderVAR = builder.get_variable('SourceFolder')
        self.Output = builder.get_object('Output').insert('end', "")
        #resize
        # self.grid_columnconfigure(0,weight=1)
        # self.resizable(True,False)
        # # self.update()
        # self.geometry(self.geometry())
        # closing function
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.quit)
        builder.connect_callbacks(self)
    
    def quit(self, event=None):
        self.mainwindow.destroy()
    
    def run(self):
        self.mainwindow.mainloop()

    def on_button1_click(self):
        self._grep_that_shit()

    def _grep_that_shit(self):
        for fname in directory: 
            if os.path.isfile(self.SourceFolderVAR.get() + os.sep + fname):
                # Full path
                r = open(self.SourceFolderVAR.get() + os.sep + fname, 'r')
                if self.SearchStringVAR in r.read():
                    # print('%s' % fname)
                    print(self.Output)

            if os.path.isfile(self.SourceFolderVAR.get() + os.sep + fname):
                # Full path
                f = open(self.SourceFolderVAR.get() + os.sep + fname, 'r')
                # Testing that F works
                # print(f)
                for line in f:
                    line = line.rstrip()
                    if re.search(self.SearchStringVAR.get(), line): 
                        # print (" - " + line )
                        print(self.Output)

#---------------------------------------------- 
if __name__ == '__main__':
    app = Application()
    app.run()