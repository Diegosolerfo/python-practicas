#Cuota de hipoteca
#Para un préstamo hipotecario se utiliza la fórmula de amortización fija:
#M=P×r(1+r)n(1+r)n−1 M = P \times \frac{r(1+r)^n}{(1+r)^n - 1}M=P×(1+r)n−1r(1+r)n​
#donde PPP es el capital, rrr la tasa mensual (tasa anual/12) y nnn el número total de cuotas (años×12).
#Entradas: capital, tasa anual (en %), plazo en años.
#Salida: cuota mensual.

#Letra	Significado
#M	Cuota mensual a pagar
#P	Capital (el préstamo que te da el banco)
#r	Tasa de interés mensual (tasa anual / 12 / 100)
#n	Número total de cuotas (años × 12)

#Paso a paso:
#1. Definir las variables, y pedir al usuario los datos
p = float(input("Ingrese el capital o cuando le van a prestar:"))
r = int(input("Ingrese la tasa mensual en %:"))
n = int(input("Ingrese el plazo en años:"))
#2. Calcular la cuota mensual usando la formula, tasa de interes mensaul r=tasa anual(en %) / 12(meses) / 
tm = r / 100 / 12
#3. Despues calcular el numero de meses n = años * 12 (meses)
a = n * 12
#4. Calcular la cuota mensual usando: M = P(capital) * r(1+r)^n / (1+r)^n - 1
M = p * (tm * (1 + tm) ** a) / ((1 + tm) ** a - 1)
#5. Imprimir los resultados
print(f"La cuota mensual es: {M:.2f} €\n con un capital de {p:.2f} €\n con una tasa de {r:.2f} %\n y un plazo de {n:.2f} años")
#6. Fin del programa