import seaborn as sns
import matplotlib.pyplot as plt

# Load the Flights dataset
flights = sns.load_dataset("flights")

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Line Plot: Yearly Trend of Airline Passengers
sns.lineplot(data=flights, x="year", y="passengers", estimator="sum", errorbar=None, marker="o", ax=axes[0, 0])
axes[0, 0].set_title("Total Passengers Per Year")

# 2. Box Plot: Monthly Passenger Distribution Over Years (Fix: Assign hue)
sns.boxplot(data=flights, x="month", y="passengers", hue="month", palette="coolwarm", legend=False, ax=axes[0, 1])
axes[0, 1].set_title("Passenger Distribution by Month")

# 3. Bar Plot: Average Monthly Passenger Count (Fix: Assign hue)
sns.barplot(data=flights, x="month", y="passengers", hue="month", estimator="mean", palette="Blues", legend=False, ax=axes[1, 0])
axes[1, 0].set_title("Average Monthly Passengers")

# 4. Heatmap: Monthly Passenger Count Over Years
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu", linewidths=0.5, ax=axes[1, 1])
axes[1, 1].set_title("Heatmap of Monthly Passengers")

# Adjust layout and display
plt.tight_layout()
plt.show()