import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("fill_data.csv")
ages = data["Age"]
dev_salaries = data["All_Devs"]
py_salaries = data["Python"]
js_salaries = data["JavaScript"]

plt.plot(ages, dev_salaries, color="#444444", linestyle="--", label="All Devs")

plt.plot(ages, py_salaries, label="Python")


overall_median = 57287

# Fill area determinned by overall_median

# plt.fill_between(ages, py_salaries, overall_median,
#                  where=(py_salaries > overall_median), interpolate=True, alpha=0.25)

# plt.fill_between(ages, py_salaries, overall_median,
#                  where=(py_salaries < overall_median), color="red", interpolate=True, alpha=0.25)

# Fill between plots
plt.fill_between(
    ages,
    py_salaries,
    dev_salaries,
    where=(py_salaries > dev_salaries),
    interpolate=True,
    alpha=0.25,
    label="Above average",
)

plt.fill_between(
    ages,
    py_salaries,
    dev_salaries,
    where=(py_salaries < dev_salaries),
    color="red",
    interpolate=True,
    alpha=0.25,
    label="Below average",
)


plt.legend()

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()
