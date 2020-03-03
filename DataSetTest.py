"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time

s_time = process_time()

test = DataSetCleanse('C:/Users/ryan/Desktop/data_cbt/shrunk_july-oct.csv', status_bar=True)
ids = list(set(test.getColumn('Account Nbr')))
titles = ['Account Nbr', 'Total Transactions', 'Account Status']
total_trans = test.num_transactions_of_each_account(status_bar=True)
acc_stat = test.encoded_account_statuses(status_bar=True)
write_csv(ids, titles, total_trans, acc_stat, filename='data_files/July-October_Transactions.csv', status_bar=True)

e_time = process_time()
print("CSV write took {} seconds to complete.".format(str(float(e_time - s_time))))
