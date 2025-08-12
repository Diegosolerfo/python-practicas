import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Graficas\\bigotes.csv")
print(df)

#Indicando los val,ores de la grafica
sns.boxplot(x="categoria", y="valor",data=df)

plt.show()