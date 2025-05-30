import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Parâmetros do modelo
total_anos = 5
total_meses = total_anos * 12
clientes_potenciais = 2000
r = 0.05            # taxa de crescimento da curva S
t0 = 30            # ponto de inflexão (mês 30)
media_inicial = 0.5  # 1 cliente a cada 2 meses
cancelamento_anual = 0.04

# Preparando datas
meses = np.arange(total_meses)
meses_formatados = [f"Ano {m//12 + 1} - Mês {m%12 + 1}" for m in meses]

# Curva S - crescimento acumulado
clientes_acumulados_s = clientes_potenciais / (1 + np.exp(-r * (meses - t0)))
novos_clientes_s = np.diff(np.insert(clientes_acumulados_s, 0, 0))

# Poisson - simulação de clientes adquiridos mensalmente
np.random.seed(42)
lambda_poisson = np.minimum(media_inicial * (1 + meses / 24), novos_clientes_s)
clientes_poisson = np.random.poisson(lam=lambda_poisson)
clientes_acumulados_p = np.cumsum(clientes_poisson)

# Aplicando cancelamento de 4% ao ano a partir do 4º ano
clientes_acumulados_s_corr = clientes_acumulados_s.copy()
clientes_acumulados_p_corr = clientes_acumulados_p.copy()

for i in range(36, total_meses):
    meses_passados = i - 36 + 1
    fator_cancelamento = (1 - cancelamento_anual / 12) ** meses_passados
    clientes_acumulados_s_corr[i] *= fator_cancelamento
    clientes_acumulados_p_corr[i] *= fator_cancelamento

# Arredondar e converter para tipos compatíveis com Excel (float padrão e int)
novos_clientes_s_rounded = np.round(novos_clientes_s, 2).astype(float)
clientes_acumulados_s_corr_rounded = np.round(clientes_acumulados_s_corr, 2).astype(float)
clientes_poisson_int = clientes_poisson.astype(int)
clientes_acumulados_p_corr_rounded = np.round(clientes_acumulados_p_corr, 2).astype(float)

# Criando o DataFrame principal
df = pd.DataFrame({
    "Mês": meses_formatados,
    "Curva S - Novos Clientes": novos_clientes_s_rounded,
    "Curva S - Acumulado Corrigido": clientes_acumulados_s_corr_rounded,
    "Poisson - Novos Clientes": clientes_poisson_int,
    "Poisson - Acumulado Corrigido": clientes_acumulados_p_corr_rounded
})

# Estatísticas descritivas (usando float para evitar problemas)
stats = df[[
    "Curva S - Novos Clientes",
    "Curva S - Acumulado Corrigido",
    "Poisson - Novos Clientes",
    "Poisson - Acumulado Corrigido"
]].agg(["sum", "mean", "std", "min", "max"]).astype(float).T

# Exportando para Excel
excel_filename = "curva_s_vs_poisson_clientes_corrigido.xlsx"
with pd.ExcelWriter(excel_filename, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Simulação", index=False)
    stats.to_excel(writer, sheet_name="Estatísticas Descritivas")

print(f"Planilha criada com sucesso: {excel_filename}")

# --- Configuração do gráfico animado ---
fig, ax = plt.subplots(figsize=(10,6))
ax.set_xlim(0, total_meses)
ax.set_ylim(0, clientes_potenciais * 1.1)
ax.set_xlabel('Mês')
ax.set_ylabel('Clientes Acumulados')
ax.set_title('Aquisição de Clientes: Curva S vs Poisson')
ax.grid(True)

line1, = ax.plot([], [], label='Curva S Corrigida', color='blue', lw=2)
line2, = ax.plot([], [], label='Poisson Corrigida', color='orange', lw=2)
txt1 = ax.text(0, 0, '', color='blue', fontsize=10, weight='bold')
txt2 = ax.text(0, 0, '', color='orange', fontsize=10, weight='bold')
ax.legend(loc='upper left')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    txt1.set_text('')
    txt2.set_text('')
    return line1, line2, txt1, txt2

def update(frame):
    x = meses[:frame+1]
    y1 = clientes_acumulados_s_corr[:frame+1]
    y2 = clientes_acumulados_p_corr[:frame+1]
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    txt1.set_position((x[-1], y1[-1]))
    txt1.set_text(f'{int(y1[-1])} clientes')
    txt2.set_position((x[-1], y2[-1]))
    txt2.set_text(f'{int(y2[-1])} clientes')
    return line1, line2, txt1, txt2

anim = FuncAnimation(fig, update, frames=total_meses, init_func=init, blit=True, interval=100)

# Salvar GIF
gif_filename = "aquisição_clientes_animacao.gif"
anim.save(gif_filename, writer=PillowWriter(fps=10))

print(f"Gráfico animado salvo como: {gif_filename}")
