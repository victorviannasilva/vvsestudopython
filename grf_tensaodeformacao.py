import matplotlib.pyplot as plt
deformacao = [0, 0.01, 0.02, 0.03, 0.05, 0.1, 0.2]  # Exemplos de dados
tensao = [0, 100, 200, 300, 400, 500, 600]           # Exemplos de dados

plt.figure(figsize=(8, 6))
plt.plot(deformacao, tensao, label='Tensão-Deformação', color='b', marker='o', linestyle='-')

# Adicionar linhas e anotações para as regiões e pontos
plt.axvline(x=0.005, color='g', linestyle='--', label='Limite de Escoamento')  # Tensão de escoamento
plt.axvline(x=0.2, color='r', linestyle='--', label='Ponto de Ruptura')        # Ponto de ruptura
plt.axhline(y=600, color='orange', linestyle='--', label='Tensão Máxima')      # Carga máxima

# Anotações no gráfico
plt.text(0.002, 300, 'Região Elástica', fontsize=12, color='green')
plt.text(0.08, 300, 'Região Plástica', fontsize=12, color='red')
plt.text(0.18, 450, 'Ponto de Ruptura', fontsize=12, color='red')  # Ajuste para evitar fora do gráfico
plt.text(0.05, 620, 'Carga Máxima', fontsize=12, color='orange')

# Definir rótulos e título
plt.xlabel('Deformação (mm/mm)', fontsize=14)
plt.title('Diagrama Tensão-Deformação', fontsize=16)
plt.ylabel('Tensão (MPa)', fontsize=14)

# Limites dos eixos
plt.xlim(0, 0.25)  # Ajuste o limite para melhor visualização
plt.ylim(0, 700)   # Aumentar o limite para evitar cortar anotações

# Adicionar uma grade e uma legenda
plt.grid(True)
plt.legend(loc='best')  # Evitar sobreposição de legenda

# Mostrar o gráfico com as anotações
plt.show()
