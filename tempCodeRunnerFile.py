import matplotlib.pyplot as plt
import plot_penguins_sb as sns
penguins=sns.load_dataset("penguins")

sns.scatterplot(data=penguins,x="bill_length",
            y="bill_depth",
            hue="species",
            style="species")
plt.show()