"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time

# s_time = process_time()

# test = DataSetCleanse('C:/Users/ryan/Desktop/data_cbt/Liberty_Transaction_Analysis_RTXN_07_01_19-10_01_2019.csv')
# ids = list(set(test.getColumn('Account Nbr')))
# titles = ['Account Nbr', 'Total Transactions', 'Account Status']
# total_trans = test.num_transactions_of_each_account()
# acc_stat = test.encoded_account_statuses()

# write_csv(ids, titles, total_trans, acc_stat, filename='data_files/July-October_Transactions.csv')

# e_time = process_time()
# print("CSV write took {} seconds to complete.".format(str(float(e_time - s_time))))


# print('  finished.')
# titles = ['Account Nbr', 'Account Status Cd']

# print('getting account numbers...')
# acc_nums = test.getColumn('Account Nbr')
# print('  finished.')
# print('getting account statuses...')
# stats = test.getColumn('Account Status Cd')
# print('  finished.')
# acc_stats = dict()
# print('making dictionary...')
# for i in range(len(acc_nums)):
#     acc_stats[acc_nums[i]] = stats[i]
# print('  finished.')

# print('writing csv...')
# write_csv(acc_nums, titles, acc_stats, filename='data_files/shrunk_jan-mar.csv')
# print('  finished.')
# e_time = process_time()
# print("CSV write took {} seconds to complete.".format(str(float(e_time - s_time))))

