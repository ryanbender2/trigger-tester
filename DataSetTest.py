"""
  Testing module for the DataSet class.
"""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
import random
import DataSet

titles = ['Account Nbr', 'Transaction Nbr', 'Transaction Effective Dt', 'Transaction Source Cd', 'Transaction Source Desc',
          'Transaction Type Cd', 'Transaction Type Desc', 'Transaction Amt', 'Balance After Tran Amt', 'Account Status Cd']
test = DataSetCleanse('data_files/test.csv')
test.setTitles(titles)

print(str(test.getColumn('Transaction Amt')[:20]) + '\nconverted\n')
d = test.str_column_to_int('Account Status Cd')
print(d)
