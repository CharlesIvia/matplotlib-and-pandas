from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import csv

plt.style.use("Solarize_Light2")

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

languages = []
popularity = []
most_common = language_counter.most_common(15)
for item in most_common:
    languages.append(item[0])
    popularity.append(item[1])

# bar chart of most popular programming language

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming languages")
plt.xlabel("Users")

plt.tight_layout()

plt.show()
