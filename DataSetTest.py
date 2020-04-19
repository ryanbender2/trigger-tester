"""Testing module for the DataSetCleanse class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
from time import process_time
from collections import Counter

dirs = [i for i in dir(DataSetCleanse) if not i.startswith('_')]
print(dirs)
# jan_mar = DataSetCleanse('C:\\Users\\ryanb\\Desktop\\CBT_Transactions_january-march_2019.csv', status_bar=True)
# jan_mar.str_column_to_float('Balance')
# jan_mar.str_column_to_float('TRANAMT')
# data = jan_mar.getDataSet(column_titles=False)

# neg_records = [data[i] for i in range(len(data)) if data[i][2] <= 0]
# print(len(neg_records))
# account_numbers = list(set(jan_mar.getColumn('Account Nbr')))
# losers = []
# for account in account_numbers:
#     act = False
#     closed = False
#     print()
#     for row in neg_records:
#         if account == row[0]:
#             print('values {}, {} | active {}'.format(account, row[1], row[1] == 'ACT'))
#             print('values {}, {}, {} | closed {}'.format(account, row[0], row[1], row[1] != 'ACT'))
#         if account == row[0] and row[1] == 'ACT':
#             act = True
#         if account == row[0] and row[1] != 'ACT':
#             closed = True
#     if act and closed:
#         losers.append(account)
# jan_mar.print_example_record()
    

