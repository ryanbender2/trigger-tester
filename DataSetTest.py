"""
  Testing module for the DataSet class.
"""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
import random
import DataSet

test = DataSetCleanse('data_files/test.csv')

f = test.encoded_account_statuses()
g = test.num_transactions_of_each_account(title_of_acc_nbr='ï»¿Account Nbr')