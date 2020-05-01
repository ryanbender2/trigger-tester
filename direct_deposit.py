"""Testing module for the DataSetCleanse class."""

from DataSetCleanse import DataSetCleanse
from DataSetCleanse import write_csv
from DataSetCleanse import chop_csv
import random
from time import process_time
from collections import Counter
import pandas as pd
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import json
from multiprocessing import Pool
import math

"""
# Getting dictionary
with open('path_to_file/person.json', 'r') as f:
    person_dict = json.load(f)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent=4))
"""


def check_for_dir_dep(one_account_list: list):
    """Based on an account's data, derive whether or not the account has a Direct Deposit.

    Arguments:
        one_account_list {list} -- All of the client's transaction data.

    Returns:
        {list} -- Summary of data found.
    """
    dd_catch_reasons = list()
    id_counter = 0
    date_col = 14
    transamt_col = 13
    for row in range(len(one_account_list)):
        working_date = datetime.strptime(one_account_list[row][date_col], '%m/%d/%Y')
        working_trans_amt = one_account_list[row][transamt_col]
        weeks_2 = working_date + timedelta(weeks=2)
        months_1 = working_date + relativedelta(months=+1)
        for verifier in range(row + 1, len(one_account_list)):
            verify_date = datetime.strptime(one_account_list[verifier][date_col], '%m/%d/%Y')
            if weeks_2 == verify_date or months_1 == verify_date:
                if working_trans_amt > 50.0:
                    verify_trans_amt = one_account_list[verifier][transamt_col]
                    if verify_trans_amt in range(int(working_trans_amt - 100.0), int(working_trans_amt + 100.0)):
                        entry_to_catch = dict()
                        
                        # add catching data to tracker
                        entry_to_catch['id'] = id_counter
                        entry_to_catch['date 1'] = str(working_date)[:10]
                        entry_to_catch['date 2'] = str(verify_date)[:10]
                        entry_to_catch['tran amount 1'] = working_trans_amt
                        entry_to_catch['tran amount 2'] = verify_trans_amt
                        
                        dd_catch_reasons.append(entry_to_catch)
                        id_counter += 1
    
    return dd_catch_reasons


def main():
    print('loading datasets...')
    files_2019 = list()
    filepaths_2019 = [
        # 'CBT_Transactions_january-march_2019.csv',
        # 'CBT_Transactions_april-june_2019.csv',
        # 'CBT_Transactions_july-october_2019.csv',
        # 'CBT_Transactions_october-december_2019.csv'
    ]
    for path in filepaths_2019: files_2019.append(DataSetCleanse('C:\\Users\\ryanb\\Desktop\\data_cbt\\%s' % path))

    one_account_list = list()
    for i in files_2019:
        acc_stat = i.encoded_account_statuses(account_status_col_title='ACCTSTATCD')
        one_account_list.append(acc_stat)

    dataset = dict() # account statuses
    for i in one_account_list:
        for row in i:
            dataset[row] = i[row]

    with open('results.json', 'r') as f:
        results = json.load(f)
    
    for acc in results:
        try:
            results[acc]["Account Status"] = dataset[acc]
        except KeyError:
            pass
    
    with open('results_added.json', 'w') as fp:
        json.dump(results, fp)
    
    print('separating dataset by accounts...')
    account_transactions_sep = dict()
    for row in dataset:
        try:
            account_transactions_sep[row[0]].append(row)
        except KeyError:
            account_transactions_sep[row[0]] = []
            account_transactions_sep[row[0]].append(row)

    stats = dict()
    account_numbers = str(len(account_transactions_sep))
    count = 1
    print('Starting search for Direct Deposit on %s accounts...' % account_numbers)
    
    with Pool(6) as p:
        check_results = p.map(check_for_dir_dep, account_transactions_sep.values())
        keys = list(account_transactions_sep.keys())
        for account_number in range(len(account_transactions_sep)):
            if check_results[account_number]:
                acc_stats = dict()
                acc_stats['direct deposit triggers found'] = len(check_results[account_number])
                acc_stats['triggers'] = check_results[account_number]
                stats[keys[account_number]] = acc_stats

    with open('results_added.json', 'w') as fp:
        json.dump(stats, fp)

def pr():
    
    num_dd = dict()
    # Getting dictionary
    with open('direct_deposit_triggers.json', 'r') as f:
        results = json.load(f)

    for acc in results:
        status = results[acc]["Account Status"]
        amm = results[acc]["direct deposit triggers found"]
        tran_amount_check = results[acc]["triggers"][0]["tran amount 2"]
        
        if status == '0' and amm > 5 and amm < 27 and tran_amount_check > 150:
            num_dd[acc] = results[acc]
    
    print(len(num_dd))
    print(json.dumps(num_dd, indent=4))
    
if __name__ == "__main__":
    # main()
    pr()