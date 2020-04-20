"""Simply UI for DataSetCleanse module."""

from breezypythongui import EasyFrame
from DataSetCleanse import DataSetCleanse as DSC
from ntpath import basename
from os import getcwd

class DataSetCleanse(EasyFrame):
    """DataSetCleanse class interface."""
    
    def __init__(self):
        """Init class."""
        super().__init__(title='DataSetCleanse')
        
        self.CSV = None
        self.addLabel(text='CSV ', row=0, column=0)
        self.CSV_path = self.addTextField(text='', row=0, column=1, width=60)
        self.addButton(text='Load', row=0, column=2, command=self.load_csv)
        
        self.addLabel(text='Working file', row=1, column=0)
        self.w_file = self.addLabel(text='None', row=1, column=1)
        
        self.outputArea = self.addTextArea(' ', row=6, column=0, columnspan=6, height=15)
        self.outputArea["state"] = "disabled"
        
        self.addLabel('Columns', 4, 0)
        self.col_vars = list()
        
        self.addLabel(text='Write new file', row=5, column=0)
        self.write_filepath = self.addTextField(text='', row=5, column=1, width=60)
        self.addButton('Write', row=5, column=2, command=self.write_file)
        self.addLabel('(Leave blank for default)', 5, 3)
    
    def _write_to_output(self, text):
        """Write new text to output area.
        
        Arguments:
            text {str} -- Text to display.
        """
        self.outputArea["state"] = "normal"
        self.outputArea.setText(text)
        self.outputArea["state"] = "disabled"
    
    def load_csv(self):
        """Load CSV file to be used."""
        path = self.CSV_path.getText() # path from user
        self.CSV_path.setText('')
        try:
            self.CSV = DSC(path) # create new DataSetCleanse object with filepath from user
            
            # update console with sample data and description of dataset
            to_output = "Loaded file: {}\n{}\n\n".format(basename(path), self.CSV.describe())
            top = ''
            for row in self.CSV.getDataSet()[:5]: top += ', '.join(row) + '\n'
            to_output += top
            self._write_to_output(to_output)
            
            self.w_file.destroy() # erase filepath
            self.w_file = self.addLabel(text=str(basename(path))[:-4], row=1, column=1)
        except FileNotFoundError as err:
            to_output = "Error loading CSV\n%s" % str(err)
            self._write_to_output(to_output)
            self.w_file.destroy()
            self.w_file = self.addLabel(text='None', row=1, column=1)
        
        # create check boxes for each column and pass each to global list
        titles = self.CSV.getTitles()
        for row in range(1, len(titles)):
            cb = self.addCheckbutton(titles[row], 4, row)
            self.col_vars.append(cb)

    def write_file(self):
        """Write csv file."""
        col_states = [(var['text'], var.isChecked()) for var in self.col_vars] # column titles and their state set from user
        dataset = self.CSV.getDataSet(column_titles=True) 
        filepath = self.write_filepath.getText() # filepath written by user
        console = self.outputArea.getText() # current console text

        # delete columns user does not want written
        for column, state in col_states:
            if not state:
                col_idx = dataset[0].index(column)
                for row in dataset: del row[col_idx]

        # write data to file
        out_location = write_csv(dataset[0], dataset[1:], filepath)
        
        # update console
        self._write_to_output(console + '\nWrote columns {} to {}!'.format(', '.join(dataset[0]), out_location))


def write_csv(col_titles, rows, filename=None):
    """Write out new csv file.
    
    Default output location -- Current working dir
    
    Arguments:
        col_titles {list} -- Titles for columns.
        columns {list} -- List of columns.
    
    Keyword Arguments:
        filename {str} -- filename. (default: current working dir)
    
    Returns:
        {str} -- Output file location.
    """
    # Check that number of column titles = number of columns
    if len(col_titles) != len(rows[0]):
        raise Exception("Number of column titles and columns are not the same.")
    
    # Find suitable filename for new file
    if not filename:    
        count = 0
        file_name_found = False
        while not file_name_found:
            attempted_filename = '{}\\Generated_CSV({}).csv'.format(str(getcwd()), str(count))
            try:
                open(attempted_filename)
                count += 1
            except FileNotFoundError:
                filename = attempted_filename
                file_name_found = True
    else:
        try:
            open(filename)
            raise Exception("Attempted write to existing file.")
        except FileNotFoundError: pass
    
    # Write lines
    nl = '\n'
    with open(filename, 'w') as file:
        file.write(','.join(col_titles) + nl)
        for row in rows: file.write(','.join(row) + nl)
    
    return filename


def main():
    """Run interface."""
    DataSetCleanse().mainloop()
    

if __name__ == "__main__":
    main()