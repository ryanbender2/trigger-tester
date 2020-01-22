"""DataSet.py: Functions as an interface for bank records.

Parameters:
csv_file (str): filepath to dataset
"""

import csv
from collections import OrderedDict


class DataSet(object):
    """
    Dataset parser
    
    :param csv_file: filepath to dataset
    :type csv_file: str
    
    """

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.__getdata__()
    
    def __getdata__(self):
        data = []  # Data from csv file, each row in csv file is an OrderedDict
        
        # Parse csv file
        csvFile = open(self.csv_file, newline='')
        parsedFile = csv.DictReader(csvFile)
        for row in parsedFile:
            strippedRow = OrderedDict(row)  # Cleaned keys
            keys = row.keys()
            for i in keys:  # runs over all keys to strip
                strippedStr = i.strip('ï»¿')
                value = row.get(i)
                strippedRow.pop(i)
                strippedRow[strippedStr] = value
            data.append(strippedRow)

        return data
    
    def getAllRecords(self):
        """getAllRecords: returns all records in dataset
            
        :params None
        :returns data: list
        """
        return self.data

    def getRecordByIndex(self, index):
        """getRecordByIndex: returns record at specified index
        
        :param index: int
        :returns record: OrderedDict
        """
        return self.data[index]
    
    def getAllValuesInCategory(self, category):
        """getAllValuesInCategory: returns all values in specifed category
        
        :param category: str
        :returns values: list
        """
        catExists = False
        
        if category in list(self.data[0].keys()):
            catExists = True
        
        if catExists:
            values = []
            for row in self.data:
                value = row.get(category)
                values.append(value)
                
            return values
        else:
            return '[getAllValuesInCategory] Error: category does not exist in dataset'
        
    def getCategories(self):
        """getCategories: returns all categories in dataset
        
        :returns categories: list
        """
        categories = []
        if len(self.data) is not 0:
            for i in self.data[0].keys():
                categories.append(i)
            
            return categories
        else:
            return '[getCategories] Error: no records in dataset'
    
    def printRecord(self, index):
        """printRecord: prints record by index, formatted
        
        :param index: int
        """
        if len(self.data) is 0:
            return '[printRecord] Error: no records in dataset'
        
        string = ''
        categories = self.getCategories()
        values = list(self.data[index].values())
        
        recordNum = '\nRecord Number ' + str(index) + '\n'

 
        return string