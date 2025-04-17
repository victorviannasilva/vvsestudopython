import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros do movimento
r = 1  # raio
omega = 2 * np.pi  # frequência angular: 1 volta por segundo
t = np.linspace(0, 2, 200)  # 2 segundos, 200 quadros

# Coordenadas do movimento circular
x = r * np.cos(omega * t)
y = r * np.sin(omega * t)

# Criando figura e eixos
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
circle_ax, proj_ax = ax

# Configurações do gráfico do círculo
circle_ax.set_xlim(-1.5, 1.5)
circle_ax.set_ylim(-1.5, 1.5)
circle_ax.set_aspect('equal')
circle_ax.set_title('Movimento Circular Uniforme')

# Configurações das projeções
proj_ax.set_xlim(0, 2)
proj_ax.set_ylim(-1.5, 1.5)
proj_ax.set_title('Projeções Harmônicas (MHS)')
proj_ax.set_xlabel('Tempo (s)')

# Elementos da animação
circle_point, = circle_ax.plot([], [], 'ro')  # ponto no círculo
circle_line, = circle_ax.plot([], [], 'r--', linewidth=0.5)  # linha até a origem
proj_x_line, = proj_ax.plot([], [], 'b-', label='x(t)')
proj_y_line, = proj_ax.plot([], [], 'g-', label='y(t)')
proj_ax.legend()

# Função para atualizar a animação
def animate(i):
    circle_point.set_data([x[i]], [y[i]])  # Wrap single values in lists
    circle_line.set_data([0, x[i]], [0, y[i]])
    proj_x_line.set_data(t[:i], x[:i])
    proj_y_line.set_data(t[:i], y[:i])
    return circle_point, circle_line, proj_x_line, proj_y_line

# Criação da animação
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=50, blit=True)

# Salvar como GIF (opcional)
ani.save('mcu_proj_mhs.gif', writer=animation.PillowWriter(fps=20))
print("GIF salvo como 'mcu_proj_mhs.gif'")
