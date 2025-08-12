import torch
import torch.nn as nn
import torch.optim as optim

# Datos de entrenamiento (x, y) → queremos que la IA aprenda la relación entre ellos
# Aquí simulamos que la ecuación secreta es: y = 2x + 3
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[5.0], [7.0], [9.0], [11.0]])

# Definimos un modelo simple de 1 neurona (como una regresión lineal)
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 1 entrada, 1 salida

    def forward(self, x):
        return self.linear(x)

# Instanciamos el modelo
model = LinearModel()

# Definimos función de pérdida (error) y optimizador
loss_function = nn.MSELoss()  # Error cuadrático medio
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Gradiente descendente

# Entrenamiento del modelo (intenta mejorar su predicción)
for epoch in range(500):
    model.train()

    # Predicción
    y_pred = model(x_train)

    # Calcular el error
    loss = loss_function(y_pred, y_train)

    # Ajustar parámetros
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f'Epoch {epoch}: Loss = {loss.item()}')

# Probar el modelo
x_test = torch.tensor([[10.0]])
prediction = model(x_test)
print(f"\nPredicción para x=10: y = {prediction.item()}")

# Ver coeficientes aprendidos
for name, param in model.named_parameters():
    print(f"{name}: {param.data}")
