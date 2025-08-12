import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Graficas\\ingresos_soñados.csv")
print(df)

#Indicando los val,ores de la grafica
sns.barplot(x="nombre", y="ingreso",data=df)

total = df["ingreso"].sum()
print(total) 

plt.show()