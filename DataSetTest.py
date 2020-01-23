"""
    Testing module for the DataSet class.
"""

import random
import DataSet

test = DataSet.DataSet('data_files/test.csv')

rdmIndex = random.randint(1, 9000)

print('\ntest.printRecord(' + str(rdmIndex) + ')\n')
print(test.printRecord(rdmIndex))
