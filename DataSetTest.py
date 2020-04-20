"""Testing module for the DataSetCleanse class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
from time import process_time
from collections import Counter

iris = DataSetCleanse('C:\\Users\\ryan\\Desktop\\machine_learning_algorithms_from_scratch\\iris.csv')
