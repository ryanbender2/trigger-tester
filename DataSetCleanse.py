"""Includes main class DataSetCleanse. To use, create object of class and initilize with csv file path.

Also includes funtion for writing csv out.
"""

import pandas as pd
import random
import progressbar
from collections import Counter

class DataSetCleanse(object):
    """DataSet Work.

    Argument:
        {str} -- Path to csv file.
    
    Keyword Arguments:
        status_bar {bool} -- Optional status bar (default: {False})
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
        # load file to pandas dataframe
        df = pd.read_csv(filename, dtype=str)

        # create dataset
        dataset = list()
        for row in df.values:
            stripped_row = [str(i).strip() for i in row]
            dataset.append(stripped_row)
        dataset.insert(0, df.columns.tolist())
        
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
            raise IndexError('Unable to find column listed: %s' % str(err))
        for row in self.__dataset:
            row[column_idx] = float(row[column_idx].strip().replace(',', ''))
    
    
    def str_column_to_int(self, column):
        """Convert string column to integer.
        
        Arguments:
            column {str} -- Title of column to convert.
        """
        try:
            column_idx = self.__titles.index(column)
        except ValueError as err:
            raise IndexError('Unable to find column listed: %s' % str(err))
        for row in self.__dataset:
            row[column_idx] = int(row[column_idx].replace(',', ''))

    
    
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
            dataset {list} -- 2D list of dataset.
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
    
    
    def num_transactions_of_each_account(self, title_of_acc_nbr='Account Nbr', status_bar=False):
        """Count of the number of transactions each account has.
        
        Keyword Arguments:
            title_of_acc_nbr {str} -- Title of column holding account numbers (default: {Account Nbr})
        
        Returns:
            Counts {dict} -- Dict with Keys = Account Number and Values = Amount of Transactions
        """
        account_nums = self.getColumn(title_of_acc_nbr)
        count_of_account_nums = dict(Counter(account_nums))
        return count_of_account_nums
    
    
    def encoded_account_statuses(self, flip_encoding=False,
                                 account_num_col_title='Account Nbr',
                                 account_status_col_title='Account Status Cd',
                                 closed_account_statuses=['APPR', 'DORM', 'NPFM', 'IACT', 'CLS', 'CO', 'CWB'],
                                 status_bar=False):
        """Encode account statuses.
        
        Keyword Arguments:
            flip_encoding {bool} -- Flips encoding (default: {False})
            account_num_col_title {str} -- Title of account number column (default: {Account Nbr})
            account_status_col_title {str} --  Title of account status column (default: {Account Status Cd})
            closed_account_statuses {list} -- Account statuses denoted as closed. (default: {APPR, DORM, NPFM, IACT, CLS, CO, CWB})
            status_bar {bool} -- Optional status bar (default: {False})
        
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
        
        if status_bar:
            # start progress bar
            print('Gathering and encoding account statuses...')
            bar = progressbar.ProgressBar(maxval=len(self.__dataset), \
                widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
            bar.start()
            count = 0
        
        for trans in self.__dataset:
            info = self.__acc_status__(trans, flip_encoding, acc_num_idx, acc_stat_idx, closed_account_statuses)
            statuses[info[0]] = info[1]
            if status_bar:
                count += 1
                bar.update(count)
        
        if status_bar:
            bar.finish()
        return statuses
    

    def print_example_record(self, index_to_print='random'):
        """Preview of dataset.
        
        Keyword Arguments:
            index_to_print {int} -- Row to preview. (default: {random})
        """
        if index_to_print == 'random':
            index = random.randint(1, len(self.__dataset))
        else:
            index = index_to_print
        string = ''
        contents = ''
        categories = self.__titles
        values = self.__dataset[index]
        longestCat = max([len(i) for i in categories])
        longestVal = max([len(str(i)) for i in values])
        recordNum = '\nRecord Number ' + str(index) + '\n'
        horizLineLen = 7 + longestCat + longestVal
        line = '-' * horizLineLen
            
        for i in range(len(values)):
            spacesCat = ' ' * (longestCat - len(categories[i]) + 1)
            spacesVal = ' ' * (longestVal - len(str(values[i])) + 1)
            SB = '| ' + categories[i] + spacesCat + '| ' + str(values[i]) + spacesVal + '|\n' + line + '\n'
            contents += SB

        string += recordNum
        string += line + '\n'
        string += contents

        print(string)
    
    
    def describe(self):
        """Describe datset, shows number of rows and columns.
        
        Returns:
            {str} -- Description of dataset.
        """
        num_cols = len(self.getTitles())
        num_rows = len(self.getDataSet(column_titles=False))
        desc = '{0} rows x {1} columns'.format(str(num_rows), str(num_cols))
        return desc
    
    
    def make_dict(self, keys, values, status_bar=False):
        """Create dictionary from dataset.
        
        Arguments:
            keys {str} -- Column title for keys
            values {str} -- Column title for values
        
        Keyword Arguments:
            status_bar {bool} -- Optional status bar (default: {False})
        
        Returns:
            {dict} -- Dictionary specified
        """
        try:
            keys_idx = self.__titles.index(keys)
            values_idx = self.__titles.index(values)
        except ValueError as err:
            print('[make_dict] Unable to find keys or values column: ' + str(err))
            exit(-1)
        
        if status_bar:
            # start progress bar
            print('Creating dictionary ({0} = {1})...'.format(keys, values))
            bar = progressbar.ProgressBar(maxval=len(self.__dataset), \
                widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
            bar.start()
            count = 0
        
        new_dict = dict()
        for row in self.__dataset:
            new_dict[row[keys_idx]] = row[values_idx]
            if status_bar:
                count += 1
                bar.update(count)
        
        if status_bar:
            bar.finish()
        return new_dict


def write_csv(IDs, col_titles, *args, **kwargs):
    """Write CSV out.
    
    How it works: Lists of unique identifiers and column titles are passed in along with dictionaries of each column.
    All dictionary keys should be in IDs.
    An example call would look like this: write_csv(Account_nbrs, col_titles, dict1, dict2, dict3, filename='example.csv')
    
    Standard output location: data_files
    
    Arguments:
        IDs {list} -- Ids for entries.
        col_titles {list} -- Titles for each column.
    
    Keyword Arguments:
        filename {str} -- Filename of new file. (example: data_files/Liberty_Trans_3.csv) (default: {default})
        status_bar {bool} -- Optional status bar (default: {False})
    """
    # Error checks
    if type(IDs) != list:
        print('[write_csv] IDs needs to be a list. IDs recieved an arg of type: ' + type(IDs))
        exit(-1)
    if len(col_titles) != (len(args) + 1):
        print('[write_csv] The number of column titles and columns are not the same.')
        exit(-1)
    for i in args:
        if type(i) != dict:
            print('[write_csv] Each argument passed in needs to a dict. ' +
                  'A list was of type: ' + type(i) + '\n' +
                  'Example usage: write_csv(Account_nbrs, col_titles, dict1, dict2, dict3, filename="example.csv")')
            exit(-1)
    
    # Find suitable filename for new file
    filename = ''
    status_bar = False
    if not kwargs:    
        count = 0
        file_name_found = False
        while not file_name_found:
            attempted_filename = 'data_files/Generated_CSV({}).csv'.format(str(count))
            try:
                t = open(attempted_filename)
                count += 1
            except FileNotFoundError:
                filename = attempted_filename
                file_name_found = True
    else:
        for key, value in kwargs.items():
            if key == 'filename':
                try:
                    t = open(value)
                    print('[write_csv] Attempted write to existing file.')
                    exit(-1)
                except FileNotFoundError:
                    filename = value
            if key == 'status_bar':
                status_bar = value

    if status_bar:
        # start progress bar
        print('Writing csv out ({})...'.format(filename))
        bar = progressbar.ProgressBar(maxval=len(IDs), \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        count = 0
    
    # Write lines
    nl = '\n'
    with open(filename, 'w') as file:
        file.write(','.join(col_titles) + nl)
        for iden in IDs:
            if status_bar:
                count += 1
                bar.update(count)
            iden_values = list()
            for col in args:
                try:
                    iden_values.append(str(col[iden]))
                except KeyError:
                    iden_values.append('')
            iden_values.insert(0, str(iden))
            file.write(','.join(iden_values) + nl)
    if status_bar:
        bar.finish()


def chop_csv(csv_filepath, nrows):
    """Shrink CSV to desired lenght. Typically used for testing and debugging.
    
    Arguments:
        csv_filepath {str} -- Path to CSV file.
        nrows {int} -- Number of rows to be written.
    """
    new_filename = csv_filepath + '_' + str(nrows) + '_rows.csv'
    df = pd.read_csv(csv_filepath, dtype=str)
    dataset = [list(row) for row in df.values]
    dataset.insert(0, [i for i in df.columns])
    with open(new_filename, 'w') as file:
        for line in dataset:
            file.write(line + '\n')