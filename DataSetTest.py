"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time


test = DataSetCleanse('C:/Users/ryanb/Desktop/data_cbt/CBT_Transactions_oct_1st-dec_31st_2019.csv')

ids = list(set(test.getColumn('Account Nbr')))
titles = ['Account Nbr', 'Total Transactions', 'Account Status']
total_trans = test.num_transactions_of_each_account()
acc_stat = test.encoded_account_statuses()

write_csv(ids, titles, total_trans, acc_stat, filename='data_files/October-December_Transactions.csv')
