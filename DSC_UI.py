"""Simply UI for DataSetCleanse module."""

from breezypythongui import EasyFrame
from DataSetCleanse import DataSetCleanse as DSC
from ntpath import basename

class DataSetCleanse(EasyFrame):
    """DataSetCleanse class interface."""
    
    def __init__(self):
        """Init class."""
        super().__init__(title='DataSetCleanse', resizable=False)
        
        self.CSV = None
        self.addLabel(text='CSV ', row=0, column=0)
        self.CSV_path = self.addTextField(text='', row=0, column=1, width=60)
        self.addButton(text='Load', row=0, column=2, command=self.load_csv)
        
        self.addLabel(text='Working file', row=1, column=0)
        self.w_file = self.addLabel(text='None', row=1, column=1)
        
        self.outputArea = self.addTextArea(' ', row=4, column=0, columnspan=3, width=50, height=15)
        self.outputArea["state"] = "disabled"
        
        # self.DSC_dir = [i for i in dir(DSC) if not i.startswith('_')]
        # for col in range(len(self.DSC_dir)):
        #     self.addButton(text=self.DSC_dir[col], row=3, column=col)
    
    def load_csv(self):
        # C:\\Users\\ryanb\\Desktop\\CBT_Transactions_january-march_2019.csv
        path = self.CSV_path.getText()
        self.CSV_path.setText('')
        try:
            self.CSV = DSC(path)
            
            self.outputArea["state"] = "normal"
            output = "Loaded file: {}\n{}".format(basename(path), self.CSV.describe())
            self.outputArea.setText(output)
            self.outputArea["state"] = "disabled"
            
            self.w_file.destroy()
            self.w_file = self.addLabel(text=str(basename(path))[:-4], row=1, column=1)
        except FileNotFoundError as err:
            output = "Error loading CSV\n%s" % str(err)
            self.outputArea.setText(output)
            self.w_file.destroy()
            self.w_file = self.addLabel(text='None', row=1, column=1)


def main():
    """Run interface."""
    DataSetCleanse().mainloop()
    

if __name__ == "__main__":
    main()