import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Graficas\\tos.csv")
print(df)

#Indicando los val,ores de la grafica
sns.lineplot(data=df, x="fecha", y="tos")

plt.plot("03-27", 91, "ro")
plt.show()