"""Interface (in progress)."""

import tkinter as tk
from DataSetCleanse import load_csv

class Application(tk.Frame):
    """Main app class.

    Returns:
        None
    """
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
        self.csv = tk.Button(self)
        self.csv.config(text='read csv', command=self.csv_file_read)
        self.csv.pack(side='top')


    def say_hi(self):
        print("hi there, everyone!")


    def csv_file_read(self):
        dataset = 'data_files/test.csv'
        csv_file = load_csv(dataset)
        print(csv_file[:5])

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()