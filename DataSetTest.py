"""
  Testing module for the DataSet class.
"""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
import random
import DataSet
from time import process_time

start_t = process_time()
test = DataSetCleanse('C:/Users/ryan/Desktop/CSIS 484/Liberty_Transaction_Analysis_3.csv')
end_t = process_time()
print('run time was {0} seconds.'.format(str(float(end_t - start_t))) + '\n\n')

g = test.getDataSet()
for i in range(5):
    print(str(g[i]))