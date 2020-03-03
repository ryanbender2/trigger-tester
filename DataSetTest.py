"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time

# s_time = process_time()

j_m = DataSetCleanse('data_files\January-March_Transactions_no_acc.csv')
totals = j_m.getColumn('S')
new_data = list()
data = j_m.getDataSet()
amount_closed_acc = totals.count('1')
count = 0
for i in data:
    if i[1] == '1':
        new_data.append(i)
    if i[1] == '0' and count != amount_closed_acc:
        new_data.append(i)
        count += 1

with open('data_files\January-March_even_split.csv', 'w') as file:
    for row in new_data:
        file.write('{0},{1}\n'.format(row[0], row[1]))
# a_j = DataSetCleanse('data_files\April-June_Transactions.csv', status_bar=True)

# total_data = list()

# jan_mar = j_m.getDataSet(column_titles=False)
# april_june = a_j.getDataSet(column_titles=False)
# jm_acc_numbers = j_m.getColumn('Account Nbr')

# for trans in april_june:
#     if trans[0] in jm_acc_numbers:
#         temp = list()
#         temp.append(trans[0])
        
#         jm_idx = jm_acc_numbers.index(trans[0])
#         jm_record = jan_mar[jm_idx]
#         new_trans_total = int(trans[1]) + int(jm_record[1])
#         temp.append(str(new_trans_total))
#         temp.append(trans[2])
        
#         total_data.append(temp)
#     else:
#         total_data.append(trans)

# with open('data_files/ggs.csv', 'w') as file:
#     file.write('Account Nbr,Total Transactions,Account Status')
#     for i in total_data:
#         file.write(','.join(i) + '\n')

# e_time = process_time()
# print("Took {} seconds to complete.".format(str(float(e_time - s_time))))

# test = DataSetCleanse('C:/Users/ryan/Desktop/data_cbt/shrunk_july-oct.csv', status_bar=True)

# ids = list(set(test.getColumn('Account Nbr')))
# titles = ['Account Nbr', 'Total Transactions', 'Account Status']
# total_trans = test.num_transactions_of_each_account(status_bar=True)
# acc_stat = test.encoded_account_statuses(status_bar=True)
# write_csv(ids, titles, total_trans, acc_stat, filename='data_files/July-October_Transactions.csv', status_bar=True)