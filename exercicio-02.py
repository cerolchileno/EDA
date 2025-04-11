import numpy as np
import matplotlib.pyplot as plt
import math

# Equação: 2x² + 2x - 6 = 0

# Coeficientes da equação
a = 2
b = 2
c = -6

# Cálculo do discriminante
delta = b**2 - 4*a*c
print(f"Discriminante (Δ) = {delta}")

# Verificação do discriminante para determinar o número de raízes reais
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui uma raiz real: x = {x}")
else:
    # Usando a fórmula de Bhaskara para encontrar as raízes
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais:")
    print(f"x₁ = {x1}")
    print(f"x₂ = {x2}")
    
    # Verificando as raízes
    verificacao_x1 = a*(x1**2) + b*x1 + c
    verificacao_x2 = a*(x2**2) + b*x2 + c
    print(f"Verificação para x₁: {verificacao_x1:.10f}")
    print(f"Verificação para x₂: {verificacao_x2:.10f}")
    
    # Plotagem da função
    x = np.linspace(x2-2, x1+2, 1000)
    y = a*(x**2) + b*x + c
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='f(x) = 2x² + 2x - 6')
    plt.plot([x1, x2], [0, 0], 'ro', markersize=6, label=f'Raízes: x₁={x1:.2f}, x₂={x2:.2f}')
    
    # Configurações do gráfico
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.title('Gráfico da Equação Quadrática 2x² + 2x - 6')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    
    plt.show()