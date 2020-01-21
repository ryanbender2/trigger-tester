"""Return a dictionary of parsed dataset

Parameters:
csv_file (str): filepath to dataset

Returns:
dict: parsed dataset

"""

import csv


class Dataset(object):
    """
    Dataset parser
    
    :param csv_file: filepath to dataset
    :type csv_file: str
    
    """
    

    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    
    def parse(self):
        data = []  # Data from csv file, each row in csv file is an OrderedDict
        
        # Parse csv file
        csvFile = open(self.csv_file, newline='')
        parsedFile = csv.DictReader(csvFile)
        for row in parsedFile:
            data.append(row)


# test
d = Dataset('data_files\Transactions_for_IACT_Accts.csv')
d.parse()