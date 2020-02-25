"""Includes main class DataSetCleanse. To use, create object of class and initilize with csv file path.

Also includes funtion for writing csv out.
"""

import pandas as pd

class DataSetCleanse(object):
    """DataSet Work.
    
    Argument:
        {str} -- path to csv file.
    """
    
    def __init__(self, filepath):
        """Init class."""
        __data = self.__load_csv__(filepath)
        self.__titles = __data[0]
        self.__dataset = __data[1:]
    
    
    def __load_csv__(self, filename):
        """Load CSV File.
        
        Arguments:
            filename {str} -- path to csv file.
        
        Returns:
            {list} -- csv file.
        """
        df = pd.read_csv(filename, dtype=str)
        dataset = [list(row) for row in df.values]
        dataset.insert(0, [i for i in df.columns])
        return dataset


    def __acc_status__(self, transaction, 
                       flip_encoding, 
                       a_n_idx,
                       a_stat_idx,
                       closed_acc_stat):
        """Convert account statuses to numaric description.
        
        Arguments:
            transaction {list} -- One row (transaction) in dataset.
            flip_encoding {bool} -- Flips encoding.
            a_n_idx {int} -- Index of account number column.
            a_stat_idx {int} --  Index of account status column.
            closed_acc_stat {list} -- Account statuses denoted as closed.
        
        Returns:
            {tuple} -- Account number, account status code.
        """
        closed_s = '1'
        open_s = '0'
        if flip_encoding:
            closed_s = '0'
            open_s = '1'
        if transaction[a_stat_idx] in closed_acc_stat:
            acc_sts = (transaction[a_n_idx], closed_s)
            return acc_sts
        acc_sts = (transaction[a_n_idx], open_s)
        return acc_sts


    def str_column_to_float(self, column):
        """Convert string column to float.
        
        Arguments:
            column {str} -- Title of column to convert.
        """
        try:
            column_idx = self.__titles.index(column)
        except ValueError as err:
            print('[str_column_to_float] Unable to find column listed: ' + str(err))
            exit(-1)
        for row in self.__dataset:
            row[column_idx] = float(row[column_idx].strip().replace(',', ''))
    
    
    def str_column_to_int(self, column):
        """Convert string column to integer.
        
        Arguments:
            column {str} -- Title of column to convert.
        
        Returns:
            {dict} -- Converted values with keys.
        """
        try:
            column_idx = self.__titles.index(column)
        except ValueError as err:
            print('[str_column_to_int] Unable to find column listed: ' + str(err))
            exit(-1)
        dataset = self.__dataset
        class_values = [row[column_idx] for row in dataset]
        unique = set(class_values)
        lookup = dict()
        for i, value in enumerate(unique):
            lookup[value] = i
        for row in dataset:
            row[column_idx] = lookup[row[column_idx]]
        return lookup
    
    
    def getTitles(self):
        """
        Get titles of csv.
        
        Returns:
            {list} -- List of column titles.
        """
        return self.__titles


    def getDataSet(self, column_titles=True):
        """
        Get dataset of csv as list.
        
        Keyword Arguments:
            column_titles {bool} -- Set to false to not include titles at top of dataset. (default: {True})
        
        Returns:
            datset {list} -- 2D list of dataset.
        """
        if column_titles:
            data = list(self.__dataset)
            data.insert(0, self.__titles)
            return data
        return self.__dataset


    def setTitles(self, titles):
        """Replace titles. List must be the same lenght as how many columns dataset has.
        
        Arguments:
            titles {list} -- New titles.
        """
        if len(titles) != len(self.__dataset[0]):
            print('[setTitles] titles must be the same lenght as number of columns in dataset.')
            exit(-1)
        self.__titles = titles


    def getColumn(self, column, title=False):
        """Get one column in __dataset.
        
        Arguments:
            column {str} -- [description]
        
        Keyword Arguments:
            title {bool} -- Returns title with column (default: {False})
        
        Returns:
            column {list} -- Column of dataset.
        """
        if column in self.__titles:
            column_in_data = list()
            if title:
                column_in_data.append(column)
            idx = self.__titles.index(column)
            for i in self.__dataset:
                column_in_data.append(i[idx])
            return column_in_data
        print('[getColumn] Unable to locate ({0}) in dataset.'.format(column))
        exit(-1)
    
    
    def num_transactions_of_each_account(self, title_of_acc_nbr='Account Nbr'):
        """Count of the number of transactions each account has.
        
        Keyword Arguments:
            title_of_acc_nbr {str} -- Title of column holding account numbers (default: {Account Nbr})
        
        Returns:
            Counts {dict} -- Dict with Keys = Account Number and Values = Amount of Transactions
        """
        account_nums = self.getColumn(title_of_acc_nbr)
        unique_account_nums = list(set(account_nums))
        account_num_count = dict(map(lambda x: [x, account_nums.count(x)], unique_account_nums))
        return account_num_count
    
    
    def encoded_account_statuses(self, flip_encoding=False,
                                 account_num_col_title='Account Nbr',
                                 account_status_col_title='Account Status Cd',
                                 closed_account_statuses=['APPR', 'DORM', 'NPFM', 'IACT', 'CLS', 'CO', 'CWB']):
        """Encode account statuses.
        
        Keyword Arguments:
            flip_encoding {bool} -- Flips encoding (default: {False})
            account_num_col_title {str} -- Title of account number column (default: {Account Nbr})
            account_status_col_title {str} --  Title of account status column (default: {Account Status Cd})
            closed_account_statuses {list} -- Account statuses denoted as closed. (default: {APPR, DORM, NPFM, IACT, CLS, CO, CWB})
        
        Returns:
            statuses {dict} -- Keys = Account numbers, Values = Account statuses
        """
        statuses = dict()
        try:
            acc_num_idx = self.__titles.index(account_num_col_title)
            acc_stat_idx = self.__titles.index(account_status_col_title)
        except ValueError as err:
            print('[encoded_account_statuses] Unable to find account number or status listed: ' + str(err))
            exit(-1)
        for trans in self.__dataset:
            info = self.__acc_status__(trans, flip_encoding, acc_num_idx, acc_stat_idx, closed_account_statuses)
            statuses[info[0]] = info[1]
        return statuses


def write_csv(dataset, filename, **args):
    """Write CSV.
    
    Arguments:
        dataset {list} -- list formatted for csv output.
        filename {str} -- File path for csv out.
    """
    with open(filename, 'w') as file:
        for line in dataset:
            file.write(','.join(line) + '\n')

   



# dataset_path = 'C:/users/ryan/Desktop/Liberty_Transaction_Analysis_3.csv'
# new_dataset = 'data_files/new_dataset.csv'


# for trans in __data:
#     if trans[1] == '0':
#         full_data.append([trans[0], '1'])
#     else:
#         full_data.append([trans[0], '0'])
# account_statuses = dict(map(__acc_status__, __data))

# for acc in unique_account_nums:
#     full_data.append([str(account_num_count[acc]), account_statuses[acc]])

# write_csv(full_data, second_dataset)
