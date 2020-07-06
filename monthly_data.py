import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)

with open('df_w_daily_entry1.pickle','rb') as read_file:
    df_2020 = pickle.load(read_file)


with open('df_2019.pickle','rb') as read_file:
    df_2019 = pickle.load(read_file)

def get_month(df, month, year):
    """
    This function returns a dataframe with only the data of the input month
    :param df: dataframe
    :param month: int
    :param year: int
    :return: dataframe
    """
    mask = ((pd.to_datetime(str(month) + '/01/' + str(year),format='%m/%d/%Y') <= df['DATE']) & (df['DATE'] < (pd.to_datetime(str(month+1) + '/01/' + str(year),format='%m/%d/%Y'))))
    month_df = df[mask]
    return month_df




def group_by_station(df, month):
    """
    This function groups the stations (lines separate) together, and lists subway ridership by station
    :param df:
    :param month:
    :return: new dataframe
    """
    grouped = df.groupby(['STATION','LINENAME'], as_index=False)
    grouped_df = grouped['DAILY ENTRIES'].sum()
    month_str = ''
    if month == 1:
        month_str = 'JAN'
    elif month == 2:
        month_str = 'FEB'
    elif month == 3:
        month_str = 'MAR'
    elif month == 4:
        month_str = 'APR'
    elif month == 5:
        month_str = 'MAY'
    elif month == 6:
        month_str = 'JUN'

    grouped_df.columns = ['STATION', 'LINENAME', month_str]
    return grouped_df



def get_all_months(df, year):
    """
    This function makes one summary dataframe that has all months' entries for each station/line combo
    :param df:
    :param year:
    :return: new dataframe
    """
    months = [1, 2, 3, 4, 5]
    month_dfs = []
    for month in months:
        month_df = get_month(df, month, year)
        new_month_df = group_by_station(month_df, month)
        month_dfs.append(new_month_df)

    final_df = month_dfs[0]
    month_dfs.remove(final_df)
    for df in month_dfs:
        final_df = final_df.merge(df, on=['STATION','LINENAME'])
    final_df = final_df.set_index(['STATION','LINENAME'])

    return final_df



all_month_2020 = get_all_months(df_2020, 2020)
all_month_2019 = get_all_months(df_2019,2019)



with open('2020_monthly_entry_by_station.pickle','wb') as to_write:
    pickle.dump(all_month_2020,to_write)


with open('2019_monthly_entry_by_station.pickle','wb') as to_write:
    pickle.dump(all_month_2019,to_write)




'''
x_axis = ['Jan','Feb','Mar','Apr','May']
y_s = df300.sum()

plt.bar(x_axis,(y_s/1000000))
plt.ylabel('Monthly ridership (millions)')
plt.xlabel('Month')
plt.title('Total Monthly MTA Ridership (Jan-May 2020)')

plt.show()

'''