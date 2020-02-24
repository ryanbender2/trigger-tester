"""
  Testing module for the DataSet class.
"""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
import random
import DataSet

test = DataSetCleanse('data_files/test.csv')

f = test.getColumn('ï»¿Account Nbr', title=True)
print(f[:20])