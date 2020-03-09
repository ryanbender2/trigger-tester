"""Testing module for the DataSet class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
import DataSet
from time import process_time
from collections import Counter

s_time = process_time()

e_time = process_time()
print("Took {} seconds to complete.".format(str(float(e_time - s_time))))
