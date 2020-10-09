from matplotlib import pyplot as plt

plt.style.use("Solarize_Light2")

# Basic chart

slices = [60, 50, 40, 30]
labels = ["Sixty", "Fourty", "Thirty", "Twenty"]
colors = ["#008fd5", "#fc4f30", "#e5ae37", "#6d904f"]
plt.pie(slices, labels=labels, colors=colors, wedgeprops={"edgecolor": "black"})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
