import seaborn as sns 
import matplotlib.pyplot as plt 
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
sns.lineplot(x=x, y=y)
plt.title("simple seaborn line chart")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()