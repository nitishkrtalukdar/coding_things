import matplotlib.pyplot as plt
import seaborn as sns
penguins=sns.load_dataset("penguins")

sns.scatterplot(data=penguins,x="bill_length_mm",
            y="bill_depth_mm",
            hue="species",
            style="species")
plt.show()