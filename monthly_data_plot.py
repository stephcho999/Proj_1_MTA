import pickle
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np

with open('2020_monthly_entry_by_station.pickle','rb') as read_file:
    df_2020 = pickle.load(read_file)
with open('2019_monthly_entry_by_station.pickle', 'rb') as read_file:
    df_2019 = pickle.load(read_file)


x_axis = ['JAN','FEB','MAR','APR','MAY']
y_2019 = (df_2019.sum()/1000000)
y_2020 = (df_2020.sum()/1000000)
y_2019_as_pct = (df_2019.sum()/df_2019.sum())
y_2020_as_pct_2019 = (df_2020.sum()/df_2019.sum())

x = np.arange(len(x_axis))
width = 0.35
'''
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
fig, ax = plt.subplots()
bar1 = ax.bar(x-width/2, y_2019, width, label = '2019')
bar2 = ax.bar(x+width/2, y_2020, width, label = '2020')

ax.set_ylabel('Ridership (millions)')
ax.set_title('Monthly MTA ridership (January-May 2019 vs 2020)')
ax.set_xticks(x)
ax.set_xticklabels(x_axis)
ax.set_xlabel('Month')
ax.legend()

fig.tight_layout()
plt.show()

fig.savefig('MTA_monthly_2019_2020.png')
'''
plt.bar(x_axis,y_2019)
plt.bar(x_axis,y_2020)
plt.xlabel('Month')
plt.ylabel('Monthly MTA ridership in millions')
plt.show()
'''