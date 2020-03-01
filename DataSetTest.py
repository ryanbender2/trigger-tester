"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time


test = DataSetCleanse('C:/Users/ryanb/Desktop/data_cbt/CBT_Transactions_oct_1st-dec_31st_2019.csv')

titles = test.getTitles()
print(str(titles))
print('\n')
test.print_example_record()
print(str(len(test.getDataSet(column_titles=False))))

# ids = [1, 2, 3, 4]
# titles = ['id', 'wow', 'nice']

# t = {
#   1: '10',
#   2: '20',
#   3: '30'
# }

# s = {
#   1: '30',
#   2: '20',
#   3: '10',
#   4: 'dude'
# }

# write_csv(ids, titles, t, s, filename='data_files/gg.csv')
