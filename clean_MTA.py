"""
Data cleaning completed through the stage of dealing with daily entry errors in dataframe
"""


import pandas as pd
import numpy as np
import pickle

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


def remove_division_change_cols(df):
    """
    This function removes the division column and reformats column names
    :param df: dataframe
    :return: df
    """
    del df['DIVISION']
    df.columns = ['C/A', 'UNIT', 'SCP', 'STATION', 'LINENAME', 'DATE', 'TIME', 'DESC', 'ENTRIES', 'EXITS']
    return df



def time_series(df):
    """
    This function turns the date and time into datetime objects
    :param df: dataframe
    :return: dataframe
    """
    df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'], format='%m/%d/%Y %H:%M:%S' )
    df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y')



def group_turnstiles(df):
    """
    This function groups entries of unique turnstiles, and makes a new dataframe with the first log of each day
    :param df: dataframe
    :return: new dataframe
    """
    df_grouped = df.groupby(['STATION', 'LINENAME', 'UNIT', 'SCP', 'DATE'], as_index=False)['ENTRIES'].first()
    return df_grouped



def view_specific_station(df, station):
    mask = (df['STATION'] == station)
    df2 = df[mask]
    return df2



def prev_entries(df):
    """
    This function creates a new column 'PREV ENTRIES' which takes the value of 'ENTRIES' from the previous row
    :param df:
    :return:
    """
    df['PREV ENTRIES'] = df.groupby(['STATION', 'LINENAME', 'UNIT', 'SCP'])['ENTRIES'].shift(1)
    df.dropna(subset=['PREV ENTRIES'], inplace=True)
    df['PREV ENTRIES'] = df['PREV ENTRIES'].astype(int)
    return df



def daily_counter(row):
    """
    This function takes each row of a dataframe and calculates daily entries
    :param row: row of dataframe
    :return: daily entries in (int)
    """
    counter = row['ENTRIES'] - row['PREV ENTRIES']
    return counter



def daily_counter_fixer(row, max_count = 15000):
    """
    This function fixes potential errors in dataframe ['DAILY ENTRIES']
    :param df:
    :return:
    """
    og = row['DAILY ENTRIES']
    if abs(og) > max_count:
        if row['ENTRIES'] < 2000:
            return row['ENTRIES']
        else:
            return 0
    elif og < 0:
        return -(row['DAILY ENTRIES'])
    else:
        return row['DAILY ENTRIES']



def outlier_checker(df):
    outliers = []
    for index, row in df.iterrows():
        if abs(row['DAILY ENTRIES']) > 10000:
            outliers.append(row)
    return outliers



def sum_stations(df):
    grouped_df = df.groupby(['STATION','LINENAME'])['DAILY ENTRIES'].sum()
    return grouped_df


'''
*** for 2020
week_nums2 = [200606,200530,200523,200516,200509,200502, 200425,200418,200411,200404,200328,200321,200314,200307,200229,200222,200215,200208,200201,200125,200118,200111,200104,191228]
#week_nums = [191214, 191207]
# extract data from MTA website
#df = get_data(week_nums)
df10 = get_data(week_nums2)
time_series(df10)
df11 = group_turnstiles(df10)
df12 = prev_entries(df11)
df12['DAILY ENTRIES'] = df12.apply(daily_counter, axis = 1)
df12['DAILY ENTRIES'] = df12.apply(daily_counter_fixer, axis=1)


with open('df_w_daily_entry1.pickle','wb') as to_write:
    pickle.dump(df12,to_write)
'''
week_nums_2019 = [181229,190105,190112,190119,190126,190202,190209,190216,190223,190302,190309,190316,190323,190330,190406,190413,190420,190427,190504,190511,190518,190525,190601]

df_2019 = get_data(week_nums_2019)
time_series(df_2019)
df_2019_grouped = group_turnstiles(df_2019)
df_2019_w_prev = prev_entries(df_2019_grouped)
df_2019_w_prev['DAILY ENTRIES'] = df_2019_w_prev.apply(daily_counter, axis = 1)
df_2019_w_prev['DAILY ENTRIES'] = df_2019_w_prev.apply(daily_counter_fixer, axis=1)

with open('df_2019.pickle','wb') as to_write:
    pickle.dump(df_2019_w_prev,to_write)

