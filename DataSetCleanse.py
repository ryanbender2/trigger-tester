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
    if transaction[1] in ['APPR', 'DORM', 'NPFM',
                           'IACT', 'CLS', 'CO', 'CWB']:
        acc_sts = (transaction[0], '1')
        return acc_sts
    acc_sts = (transaction[0], '0')
    return acc_sts


dataset_path = 'C:/users/ryan/Desktop/Liberty_Transaction_Analysis_3.csv'
new_dataset = 'data_files/new_dataset.csv'


csv1 = load_csv(dataset_path)
titles = csv1[0]
data = csv1[1:]


# csv2 = load_csv(new_dataset)
# titles2 = csv2[0]
# data2 = csv2[1:]

# # Account Number
# account_nums = [i[0] for i in data]
# unique_account_nums = list(set(account_nums))
# account_num_count = dict(map(lambda x: [x, account_nums.count(x)], unique_account_nums))

# # Account Status
# full_data = list()

# for trans in data:
#     if trans[1] == '0':
#         full_data.append([trans[0], '1'])
#     else:
#         full_data.append([trans[0], '0'])
# account_statuses = dict(map(__acc_status__, data))

# for acc in unique_account_nums:
#     full_data.append([str(account_num_count[acc]), account_statuses[acc]])

# write_csv(full_data, second_dataset)
