import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic = sns.load_dataset("titanic")

# Set figure size
plt.figure(figsize=(15, 10))

# 1. Scatter Plot
plt.subplot(3, 3, 1)
sns.scatterplot(data=titanic, x="age", y="fare", hue="sex")
plt.title("Scatter Plot: Age vs Fare")

# 2. Line Plot
plt.subplot(3, 3, 2)
sns.lineplot(data=titanic, x="age", y="fare", estimator="mean")
plt.title("Line Plot: Average Fare by Age")

# 3. Bar Plot
plt.subplot(3, 3, 3)
sns.barplot(data=titanic, x="class", y="fare", hue="sex")
plt.title("Bar Plot: Class vs Fare")

# 4. Histogram
plt.subplot(3, 3, 4)
sns.histplot(data=titanic, x="age", bins=20, kde=True)
plt.title("Histogram: Age Distribution")

# 5. Box Plot
plt.subplot(3, 3, 5)
sns.boxplot(data=titanic, x="class", y="age", hue="sex")
plt.title("Box Plot: Age Distribution by Class")

# 6. Violin Plot
plt.subplot(3, 3, 6)
sns.violinplot(data=titanic, x="class", y="age", hue="sex", split=True)
plt.title("Violin Plot: Age Distribution by Class")

# 7. Heatmap (Correlation)
plt.subplot(3, 3, 7)
corr_matrix = titanic.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Heatmap: Titanic Correlation")

# 8. Count Plot
plt.subplot(3, 3, 8)
sns.countplot(data=titanic, x="class", hue="sex")
plt.title("Count Plot: Passengers per Class")

# 9. Pair Plot (Displayed Separately for Clarity)
plt.figure(figsize=(8, 6))
sns.pairplot(titanic, hue="sex", diag_kind="kde")
plt.suptitle("Pair Plot: Titanic Dataset", y=1.02)

# Show all plots
plt.tight_layout()
plt.show()
