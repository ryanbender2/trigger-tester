"""
  Testing module for the DataSet class.
"""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
import random
import DataSet

test = DataSetCleanse('data_files/test.csv')

f = test.num_transactions_of_each_account()
print(str(list(f.values())[:20]))