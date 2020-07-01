"""
Project goals: analyze y-o-y change for MTA ridership & citibike ridership
               break down by neighborhood

First load up the data (for the whole half year)
Filter out for certain turnstile (single turnstile data with all months)
subtract entries first of this month from first of next month and store in new df
Add all turnstile data together for each month's ridership data

Categorize turnstiles into neighborhoods
"""



import pandas as pd
import numpy as np

#prevents trailing elipses
pd.set_option('display.max_rows', None)



def get_data(week_nums):
    """
    Function that allows us to extract data from MTA website for given weeks
    :param week_nums: list of dates for which MTA data will be extracted
    :return: Dataframe
    """
    url = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_{}.txt'
    dfs = []

    for week_num in week_nums:
        file_url = url.format(week_num)
        dfs.append(pd.read_csv(file_url))

    return pd.concat(dfs)




def check_for_corrupt(df):
    """
    This function checks for empty values or null values in the dataframe
    :param df: dataframe
    :return: n/a
    """
    df2 = df.groupby('STATION').count()
    for index, row in df2.iterrows():
        col = df2.columns[0]
        for column in df2.columns:
            if row[col] != row[column]:
                print('value error')
            elif row[column] == np.nan:
                print('nan values')
            else:
                pass



def make_month_column(df):
    """
    Based on data column, creates a separate column 'month'
    :param df: dataframe
    :return: none
    """
    date = df['DATE']
    months = []
    for dat in date:
        month = dat[:2]
        months.append(month)
    df['MONTH'] = months
    return df



def select_month(df, month):
    """
    Selects data for input month
    :param df: dataframe
    :param month: month
    :return: dataframe with only specified month
    """
    str_month = str(month)
    return df.loc[df['MONTH'] == str_month]



def isolate_turnstile(df):
    """
    Calculates total entries for each turnstile for given timeframe
    :param df:
    :return:
    """
    grouped = df.groupby(by=['STATION', 'C/A', 'SCP'])
    grouped_min_max = grouped['ENTRIES'].agg(['min','max'])
    grouped_min_max['Entries'] = grouped_min_max['max']-grouped_min_max['min']
    return grouped_min_max

def check_for_outliers(grouped):
    """
    Checks for outliers in the data
    :param grouped: groupby object with turnstiles sorted
    :return:
    """
    mean_entry = grouped['Entries'].mean()
    std_entry = grouped['Entries'].std()
    entries = grouped['Entries']
    for entry in entries:
        if entry > mean_entry + 3*(std_entry):
            print(entry)



def add_turnst_entries(grouped):
    sum_entries = grouped['Entries'].sum()
    return sum_entries

week_nums = [200104, 191228, 191221, 191214, 191207]
df = get_data(week_nums)
df2 = make_month_column(df)
dec_month_df = select_month(df2, 12)
grouped_turnst = isolate_turnstile(dec_month_df)
check_for_outliers(grouped_turnst)
#print(add_turnst_entries(grouped_turnst))






'''
Objective: create dataframes each for a specific month
for i in range(1,7):
    single_month_df_list = []
    single_month_df = select_month(df2, i)
    single_month_df_list.append(single_month_df)
    
for single_month_df in single_month_df_list:
    total_entries_list = []
    total_entries_all_turnst = isolate_turnstile(single_month_df)
    total_entries_list.append(total_entries_all_turnst)
    
'''


