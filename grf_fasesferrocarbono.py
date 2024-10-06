# Criando o gráfico para o diagrama de fases Fe-C (simplificado).

# Re-importando bibliotecas após reset do ambiente
import matplotlib.pyplot as plt

# Diagrama de fases do ferro puro (simplificado)
# Temperatura (Celsius) para cada fase
temperaturas = [0, 912, 1394, 1538, 1600]
fases = ['Ferrita (α)', 'Austenita (γ)', 'Ferrita δ', 'Líquido']

# Criando a figura
plt.figure(figsize=(8, 6))

# Plotando o diagrama de fases
plt.plot([0, 912], [0, 912], label='Ferrita (α)', color='blue')
plt.plot([912, 1394], [912, 1394], label='Austenita (γ)', color='green')
plt.plot([1394, 1538], [1394, 1538], label='Ferrita δ', color='red')
plt.plot([1538, 1600], [1538, 1600], label='Líquido', color='orange')

# Adicionando as fases
plt.text(300, 450, 'Ferrita (α)', fontsize=12, color='blue')
plt.text(1000, 1150, 'Austenita (γ)', fontsize=12, color='green')
plt.text(1450, 1450, 'Ferrita δ', fontsize=12, color='red')
plt.text(1550, 1570, 'Líquido', fontsize=12, color='orange')

# Configurações do gráfico
plt.title('Diagrama de Fases do Ferro Puro', fontsize=16)
plt.xlabel('Temperatura (°C)', fontsize=14)
plt.ylabel('Comportamento do Ferro', fontsize=14)
plt.grid(True)
plt.legend(loc='upper left')

# Exibir o gráfico
plt.show()
