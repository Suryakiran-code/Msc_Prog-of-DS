# Seaborn is a powerful Python library for creating statistical graphics.
#  Seaborn offers a simple, declarative API that allows you to create complex visualizations with minimal code.
"""
import seaborn as sns 

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a relational plot
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

Types of Plots

Relational plots: (e.g., relplot, scatterplot).

Categorical plots: Visualize data grouped by categories (e.g., catplot, boxplot, violinplot, swarmplot).

Distribution plots: Examine univariate or bivariate distributions (e.g., displot, kdeplot).

Regression plots: Add regression lines to scatter plots to highlight trends (regplot).

Matrix plots: Visualize data in matrix form, such as heatmaps.

Multi-plot grids: Create grids of plots for comparing multiple variables or subsets (FacetGrid, PairGrid).

"""
#Seaborn is ideal for exploratory data analysis and for creating visually appealing, informative statistical graphics with minimal effort.