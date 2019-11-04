"""Return a dictionary of parsed dataset

Parameters:
csv_file (str): filepath to dataset

Returns:
dict: parsed dataset

"""


class Dataset(object):
    """
    Dataset parser
    
    :param csv_file: filepath to dataset
    :type csv_file: str
    
    """
    

    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    
    def parse(self):
        None
