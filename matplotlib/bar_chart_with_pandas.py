from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd
import csv

plt.style.use("Solarize_Light2")


data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]
print(lang_responses)

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))


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
