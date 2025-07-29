import matplotlib.pyplot as plt
from main import count_devs

# Data
languages = ["C++", "PHP", "Javascript", "Python", "Go", "Typescript", "Ruby", "Java"]
dev_counts = count_devs

# Create bar chart
plt.bar(languages, dev_counts, color="skyblue",edgecolor="black",linewidth = 0.62)

# Add numbers on top of bars
for i in range(len(languages)):
    plt.text(i,dev_counts[i]+1, str(dev_counts[i]), ha="center" )

# Add labels and title
plt.title("Number of Developers by Language")
plt.xlabel("Programming Languages")
plt.ylabel("Number of Developers")
plt.xticks(rotation=45)

# Show chart
plt.show()
