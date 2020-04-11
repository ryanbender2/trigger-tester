"""Interface (in progress)."""

import tkinter as tk
from time import sleep

class Application(tk.Frame):
    """Main app class.

    Returns:
        None
    """
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.hi_there_button()
        self.quit_button()
        self.csv_button()
        self.load_csv_button_entry()


    def hi_there_button(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
    
    
    def quit_button(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    
    def csv_button(self):
        self.csv = tk.Button(self)
        self.csv.config(text='read csv', command=self.csv_file_read)
        self.csv.pack(side='top')
    
    
    def load_csv_button_entry(self):
        self.u_in_filepath = tk.Entry(self)
        self.u_in_filepath.configure()
        self.u_in_filepath.pack(side='right')
        
        self.load_csv = tk.Button(self)
        self.load_csv.config(text='Load CSV', command=self.csv_load)
        self.load_csv.pack(side='left')
        
    def say_hi(self):
        print("hi there, everyone!")


    def csv_file_read(self):
        dataset = 'data_files/test.csv'
        csv_file = load_csv(dataset)
        print(csv_file[:5])
        
    
    def csv_load(self):
        self.csv_err1 = tk.Label(self)
        self.csv_err1.config(text='Please enter in path to csv file.')
        self.csv_err1.pack()
        self.csv_err1.pack_forget()

        self.csv_success = tk.Label(self)
        self.csv_success.config(text='Loaded CSV file')

        self.csv_err2 = tk.Label(self)
        self.csv_err2.config(text='Failed to load CSV file')

        dataset = self.u_in_filepath.get()

        try:
            csv_file = load_csv(dataset)
        except Exception:
            self.csv_err1.pack()
            sleep(3)
            self.csv_err1.pack_forget()
        
        if csv_file is not None:
            self.csv_success.pack()
            sleep(3)
            self.csv_success.pack_forget()
        else:
            self.csv_err2.pack()
            sleep(3)
            self.csv_err2.pack_forget()
            

def main():
    """Run GUI."""
    root = tk.Tk()
    root.geometry('400x400')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()