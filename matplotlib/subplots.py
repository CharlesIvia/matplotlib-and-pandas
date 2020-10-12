
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('fill_data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


fig, ax = plt.subplots(2, sharex=True)

ax[0].plot(ages, py_salaries, label='Python')
ax[0].plot(ages, js_salaries, label='JavaScript')

ax[1].plot(ages, dev_salaries, color='#444444',
           linestyle='--', label='All Devs')

ax[0].legend()
ax[1].legend()

ax[0].set_title('Median Salary (USD) by Age')
ax[1].set_xlabel('Ages')
ax[0].set_ylabel('Median Salary (USD)')
ax[1].set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
