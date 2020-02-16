"""Collection of methods for DataSet Work.

Returns:
    None
"""

from csv import reader


def load_csv(filename):
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


def str_column_to_float(dataset, column):
    """Convert string column to float.
    
    Arguments:
        dataset {list} -- Parsed dataset.
        column {int} -- Index of column to convert.
    """
    for row in dataset:
        row[column] = float(row[column].strip())


def str_column_to_int(dataset, column):
    """Convert string column to integer.
    
    Arguments:
        dataset {list} -- Parsed dataset.
        column {int} -- Index of column to convert.
    
    Returns:
        {dict} -- Converted values with keys.
    """
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


def write_csv(dataset, filename):
    """Write CSV.
    
    Arguments:
        dataset {list} -- list formatted for csv output.
        filename {str} -- File path for csv out.
    """
    with open(filename, 'w') as file:
        for line in dataset:
            file.write(','.join(line) + '\n')

   
def __acc_status__(transaction: list):
    """Convert account statuses to numaric description.
    
    Arguments:
        transaction {list} -- One row (transaction) in dataset.
    
    Returns:
        {tuple} -- Account number, account status code.
    """
    if type(transaction) != list:
        raise TypeError('Type must be list')
    if transaction[-1] in ['APPR', 'DORM', 'NPFM',
                           'IACT', 'CLS', 'CO', 'CWB']:
        acc_sts = (transaction[0], '1')
        return acc_sts
    acc_sts = (transaction[0], '0')
    return acc_sts


dataset_path = 'data_files\Transactions_for_IACT_Accts.csv'
new_dataset = 'data_files/new_dataset.csv'
second_dataset = 'data_files/second_dataset.csv'
# csv1 = load_csv(dataset_path)
# titles1 = csv1[0]
# data1 = csv1[1:]

# csv2 = load_csv(new_dataset)
# titles2 = csv2[0]
# data2 = csv2[1:]
print(__acc_status__(10))
# # Account Number
# account_nums = [i[0] for i in data]
# unique_account_nums = list(set(account_nums))
# account_num_count = list(map(lambda x: [x, account_nums.count(x)], unique_account_nums))

# # Account Status
# full_data = list()
# account_statuses = dict(map(__acc_status__, data1))
# trans_amounts = dict(data2)

# totals_keys = trans_amounts.keys()

# for account in totals_keys:
#     full_data.append([account, trans_amounts[account], account_statuses[account]])

# write_csv(full_data, second_dataset)