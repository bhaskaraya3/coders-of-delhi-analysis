import matplotlib.pyplot as plt
from main import avg_C_devs,avg_sal_JavaScript,avg_sal_py

# Data
sal = [avg_sal_JavaScript,avg_sal_py,avg_C_devs]
lang = ["JavaScript", "Python", "C++"]
colors = ["#66c2a5", "#fc8d62", "#8da0cb"]
explode = [0.1, 0.0, 0.0]  # Highlight JavaScript

# Title
plt.title("Average Salaries of Developers", fontsize=16, fontweight='bold')

# Pie Chart
plt.pie(
    sal,
    labels=[""] * len(lang),  # No labels inside slices
    colors=colors,
    explode=explode,
    shadow=True,
    radius=0.7,
    autopct="%0.1f%%",  # Only percentage shown
    wedgeprops={'edgecolor': "white", "linewidth": 2},
    textprops={"fontsize": 11}
)

# Legend: show name + salary
plt.legend(
    [f"{l}: ₹{s:,}" for l, s in zip(lang, sal)],
    title="Languages & Salaries",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=11,
    title_fontsize=12
)

# Layout fix
plt.tight_layout()
plt.show()
