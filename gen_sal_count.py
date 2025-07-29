import matplotlib.pyplot as plt
from main import avg_sal_gen

sal = avg_sal_gen
gen = ["Female", "Male"]
colors = ["#ff9999", "#66b3ff"]

plt.title("Average Salary by Gender")
plt.ylabel("Average Salary")
plt.xlabel("Gender")

bars = plt.bar(gen, sal, color=colors, edgecolor="black", linewidth=0.65)
# Add salary values on top of each bar
for i in range(len(sal)):
    plt.text(i, sal[i] + 1000, f"{sal[i]}", ha='center', fontsize=9)



plt.show()
