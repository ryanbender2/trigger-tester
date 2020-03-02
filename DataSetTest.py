"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time

s_time = process_time()

test = DataSetCleanse('C:/Users/ryan/Desktop/data_cbt/CBT_Transactions_oct_1st-dec_31st_2019.csv')
print('Loaded file...')
ids = list(set(test.getColumn('Account Nbr')))
print('Gathered Ids...')
titles = ['Account Nbr', 'Total Transactions', 'Account Status']
total_trans = test.num_transactions_of_each_account()
print('Calculated transaction totals...')
acc_stat = test.encoded_account_statuses()
print('Gathered account statuses...')

write_csv(ids, titles, total_trans, acc_stat, filename='data_files/October-December_Transactions.csv')
print('Wrote file...finished.\n')

e_time = process_time()
print("CSV write took {} seconds to complete.".format(str(float(e_time - s_time))))
