"""Includes main class DataSetCleanse. To use, create object of class and initilize with csv file path.

Also includes funtion for writing csv out.
"""

from csv import reader

class DataSetCleanse(object):
    """DataSet Work.
    
    Argument:
        {str} -- path to csv file.
    """
    
    def __init__(self, filepath):
        """Init class."""
        data = self.__load_csv__(filepath)
        self.titles = data[0]
        self.dataset = data[1:]
    
    
    def __load_csv__(self, filename):
        """Load CSV File.
        
        Arguments:
            filename {str} -- path to csv file.
        
        Returns:
            {list} -- csv file.
        """
        dataset = list()
        with open(filename, 'r') as file:
            csv_reader = reader(file)
            for row in csv_reader:
                if not row:
                    continue
                dataset.append(row)
        return dataset


    def __acc_status__(self, transaction):
        """Convert account statuses to numaric description.
        
        Arguments:
            transaction {list} -- One row (transaction) in dataset.
        
        Returns:
            {tuple} -- Account number, account status code.
        """
        if type(transaction) != list:
            raise TypeError('Type must be list')
        if transaction[1] in ['APPR', 'DORM', 'NPFM',
                            'IACT', 'CLS', 'CO', 'CWB']:
            acc_sts = (transaction[0], '1')
            return acc_sts
        acc_sts = (transaction[0], '0')
        return acc_sts


    def str_column_to_float(self, column):
        """Convert string column to float.
        
        Arguments:
            column {int} -- Index of column to convert.
        """
        for row in self.dataset:
            row[column] = float(row[column].strip())
    
    
    def str_column_to_int(self, column):
        """Convert string column to integer.
        
        Arguments:
            column {int} -- Index of column to convert.
        
        Returns:
            {dict} -- Converted values with keys.
        """
        dataset = self.dataset
        class_values = [row[column] for row in dataset]
        unique = set(class_values)
        lookup = dict()
        for i, value in enumerate(unique):
            lookup[value] = i
        for row in dataset:
            row[column] = lookup[row[column]]
        return lookup
    
    
    def getTitles(self):
        """
        Get titles of csv.
        
        Returns:
            {list} -- List of column titles.
        """
        return self.titles


    def getDataSet(self, column_titles=True):
        """
        Get dataset of csv as list.
        
        Keyword Arguments:
            column_titles {bool} -- Default true, set to false to not
                                    include titles at top of dataset. (default: {True})
        
        Returns:
            datset {list} -- 2D list of dataset.
        """
        if column_titles:
            data = list()
            data.append(self.titles)
            data.append(self.dataset)
            return data
        return self.dataset

    
    def setTitles(self, titles):
        """Replace titles. List must be the same lenght as how many columns dataset has.
        
        Arguments:
            titles {list} -- New titles.
        """
        if len(titles) != len(self.dataset[0]):
            print('[setTitles] titles must be the same lenght as number of columns in dataset.')
            exit(-1)
        self.titles = titles


    def getColumn(self, column, title=False):
        """Get one column in dataset.
        
        Arguments:
            column {str} -- [description]
        
        Keyword Arguments:
            title {bool} -- Returns title with column (default: {False})
        
        Returns:
            column {list} -- Column of dataset.
        """
        if column in self.titles:
            column_in_data = list()
            if title:
                column_in_data.append(column)
            idx = self.titles.index(column)
            for i in self.dataset:
                column_in_data.append(i[idx])
            return column_in_data
        print('[getColumn] Unable to locate ({0}) in dataset.'.format(column))
        exit(-1)
    
    
    def num_transactions_of_each_account(self, title_of_acc_nbr='Account Nbr'):
        """Count of the number of transactions each account has.
        
        Keyword Arguments:
            title_of_acc_nbr {str} -- Title of column holding account numbers (default: {'Account Nbr'})
        
        Returns:
            Counts {dict} -- Dict with Keys = Account Number and Values = Amount of Transactions
        """
        account_nums = self.getColumn(title_of_acc_nbr)
        unique_account_nums = list(set(account_nums))
        account_num_count = dict(map(lambda x: [x, account_nums.count(x)], unique_account_nums))
        return account_num_count


def write_csv(dataset, filename):
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


# for trans in data:
#     if trans[1] == '0':
#         full_data.append([trans[0], '1'])
#     else:
#         full_data.append([trans[0], '0'])
# account_statuses = dict(map(__acc_status__, data))

# for acc in unique_account_nums:
#     full_data.append([str(account_num_count[acc]), account_statuses[acc]])

# write_csv(full_data, second_dataset)
