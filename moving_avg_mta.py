import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('df_2020.pickle','rb') as read_file:
    df_2020 = pickle.load(read_file)


with open('df_2019.pickle','rb') as read_file:
    df_2019 = pickle.load(read_file)

#groupby station and linename, then calculate 5 day rolling average mean

df_2020.drop(columns = ['PREV ENTRIES','ENTRIES'],inplace=True)
df_2019.drop(columns = ['PREV ENTRIES','ENTRIES'],inplace=True)

print(df_2019)
print(df_2020)


def prev_days(df):
    """
    This function creates two columns for the previous two days' entries
    :param df:
    :return:
    """
    #df = df.groupby(['STATION','LINENAME'])['DAILY ENTRIES'].sum()
    df = df.groupby(['STATION', 'LINENAME', 'DATE'], as_index=False)['DAILY ENTRIES'].sum()
    df['PREV DAY'] = df.groupby(['STATION', 'LINENAME'])['DAILY ENTRIES'].shift(1)
    df['TWO DAYS PRIOR'] = df.groupby(['STATION','LINENAME'])['DAILY ENTRIES'].shift(2)
    df['THREE DAYS PRIOR'] = df.groupby(['STATION','LINENAME'])['DAILY ENTRIES'].shift(3)
    df['FOUR DAYS PRIOR'] = df.groupby(['STATION','LINENAME'])['DAILY ENTRIES'].shift(4)
    df['FIVE DAYS PRIOR'] = df.groupby(['STATION', 'LINENAME'])['DAILY ENTRIES'].shift(5)
    df['SIX DAYS PRIOR'] = df.groupby(['STATION', 'LINENAME'])['DAILY ENTRIES'].shift(6)
    df.dropna(subset=['PREV DAY','TWO DAYS PRIOR','THREE DAYS PRIOR','FOUR DAYS PRIOR','FIVE DAYS PRIOR','SIX DAYS PRIOR'], inplace=True)
    return df


def rolling_average(df):
    df['ROLLING AVERAGE'] = (df['DAILY ENTRIES'] + df['PREV DAY'] + df['TWO DAYS PRIOR'] + df['THREE DAYS PRIOR'] + df['FOUR DAYS PRIOR'] + df['FIVE DAYS PRIOR'] + df['SIX DAYS PRIOR'])/7
    return df



df_2020 = prev_days(df_2020)
df_2019 = prev_days(df_2019)

df_2020 = rolling_average(df_2020)
df_2019 = rolling_average(df_2019)


def clean_up(df, year):
    df.drop(columns=['DAILY ENTRIES','PREV DAY','TWO DAYS PRIOR'],inplace=True)
    mask = ((pd.to_datetime('01/01/' + str(year), format='%m/%d/%Y') <= df['DATE']) & (df['DATE'] < (pd.to_datetime('06/01/' + str(year), format='%m/%d/%Y'))))
    df = df[mask]

    return df

df_2020 = clean_up(df_2020,2020)
df_2019 = clean_up(df_2019,2019)


def sum_all_station(df):
    df = df.groupby(['DATE']).agg({'ROLLING AVERAGE':'sum'}).astype(int)
    return df

df_2019 = sum_all_station(df_2019)
df_2020 = sum_all_station(df_2020)



def days_column(df):
    df['DAYS AFTER JAN 1ST'] = pd.Series(np.arange(0, len(df)),index=df.index)
    return df

df_2020 = days_column(df_2020)
df_2019 = days_column(df_2019)


df_2020 = df_2020.set_index(['DAYS AFTER JAN 1ST'])
df_2019 = df_2019.set_index(['DAYS AFTER JAN 1ST'])

def in_millions(df):
    df['ROLLING AVERAGE'] = df['ROLLING AVERAGE'] / 1000000
    return df

df_2020 = in_millions(df_2020)
df_2019 = in_millions(df_2019)



#PLOTTING RAW NUMBERS

x_2019 = np.arange(0,len(df_2019),10)
x_2020 = np.arange(0,len(df_2020),10)

fig, ax = plt.subplots()
line_2019 = ax.plot(df_2019, label='2019')
line_2020 = ax.plot(df_2020, label='2020')

ax.set_xticks(x_2019)
ax.set_xticklabels(x_2019)
ax.set_xlabel('Days After Jan 1st')
ax.set_ylabel('MTA Ridership in millions')
ax.set_title('7 Day Moving Average MTA Ridership (Jan-May 2019 vs 2020)')
ax.legend()

fig.tight_layout()
plt.show()


fig.savefig('MTA_7_day_moving_avg_2019_2020.png')

# PLOTTING as % of 2019

df_2019_pct = df_2019['ROLLING AVERAGE'] / df_2019['ROLLING AVERAGE']
df_2020_pct = df_2020['ROLLING AVERAGE'] / df_2019['ROLLING AVERAGE']


x_2019 = np.arange(0,len(df_2019),10)
x_2020 = np.arange(0,len(df_2020),10)

y_ticks = [x for x in range(0,130,10)]
fig, ax = plt.subplots()

line_2020 = ax.plot(df_2020_pct*100, label='2020')

ax.set(ylim=[0,1.2])
ax.set_xticks(x_2019)
ax.set_xticklabels(x_2019)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)
ax.set_xlabel('Days After Jan 1st')
ax.set_ylabel('Ridership as % of 2019')
ax.set_title('2020 MTA Ridership as % of 2019 (January-May)')
ax.legend()

fig.tight_layout()
plt.show()


fig.savefig('MTA_2020_avg_as_pct_2019.png')



'''
x_axis = ['JAN','FEB','MAR','APR','MAY']
y_2019 = (df_2019.sum()/1000000)
y_2020 = (df_2020.sum()/1000000)
y_2019_as_pct = (df_2019.sum()/df_2019.sum())
y_2020_as_pct_2019 = (df_2020.sum()/df_2019.sum())

x = np.arange(len(x_axis))
width = 0.35

fig, ax = plt.subplots()
line1 = ax.plot(y_2019_as_pct, label='2019')
line2 = ax.plot(y_2020_as_pct_2019, label='2020')

ax.set_xticks(x)
ax.set_xticklabels(x_axis)
ax.set_ylabel('MTA ridership expressed as % of 2019')
ax.set_title('MTA Monthly Ridership 2019 vs 2020')
ax.legend()

fig.tight_layout()
plt.show()

fig.savefig('MTA_monthly_as_pct_2019.png')

'''