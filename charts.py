import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("stars.csv")

mass_list = df["mass"].tolist()
mass_list.pop(0)

radius_list = df["radius"].tolist()
radius_list.pop(0)



plt.figure()
sns.scatterplot(x = mass_list,y = radius_list)
plt.title("STAR MASS AND RADIUS")
plt.xlabel('MASS')
plt.ylabel('RADIUS')
plt.show()