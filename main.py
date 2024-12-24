import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Constantes gravitacionais e unidades astronômicas
G = 6.67430e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
AU = 1.496e11  # Unidade astronômica (m)
DAY = 24 * 3600  # Um dia em segundos

# Lista de corpos no sistema solar com dados dos planetas
bodies = [
    {"name": "Sol", "color": "#f49e12", "radius": 10, "mass": 1.989e30, "pos": np.array([0.0, 0.0], dtype=np.float64), "vel": np.array([0.0, 0.0], dtype=np.float64)},
    {"name": "Terra", "color": "#82C8E5", "radius": 8, "mass": 5.972e24, "pos": np.array([0.0, AU], dtype=np.float64), "vel": np.array([29.78e3, 0.0], dtype=np.float64)},
    {"name": "Marte", "color": "#7b0000", "radius": 8, "mass": 6.417e23, "pos": np.array([0.0, 1.524 * AU], dtype=np.float64), "vel": np.array([24.077e3, 0.0], dtype=np.float64)}
]

# Configuração da simulação
dt = DAY  # Intervalo de tempo (1 dia)
num_years = 5  # Duração da simulação em anos
steps = num_years * 365  # Total de dias a simular

# Função para calcular a força gravitacional entre dois corpos
def gravitational_force(body1, body2):
    """
    Calcula a força gravitacional entre dois corpos celestes.

    Args:
        body1 (dict): Dados do primeiro corpo (massa, posição, etc.)
        body2 (dict): Dados do segundo corpo (massa, posição, etc.)

    Returns:
        np.array: Vetor de força entre os dois corpos
    """
    r_vec = body2["pos"] - body1["pos"]
    r_mag = np.linalg.norm(r_vec)  # Magnitude da distância entre os corpos
    force_mag = G * body1["mass"] * body2["mass"] / r_mag**2  # Magnitude da força gravitacional
    force_vec = force_mag * (r_vec / r_mag)  # Vetor da força gravitacional
    return force_vec

# Simulação do movimento dos corpos
positions = {i: [body["pos"].copy()] for i, body in enumerate(bodies)}
for _ in range(steps):
    forces = {i: np.array([0.0, 0.0], dtype=np.float64) for i in range(len(bodies))}  # Inicializa as forças como zero

    # Calcular forças gravitacionais entre os corpos
    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if i != j:  # Ignora a interação de um corpo consigo mesmo
                forces[i] += gravitational_force(body1, body2)  # Soma as forças gravitacionais

    # Atualizar posições e velocidades dos corpos
    for i, body in enumerate(bodies):
        acceleration = forces[i] / body["mass"]  # Calcula a aceleração
        body["vel"] += acceleration * dt  # Atualiza a velocidade
        body["pos"] += body["vel"] * dt  # Atualiza a posição
        positions[i].append(body["pos"].copy())  # Armazena a nova posição

# Visualização com matplotlib
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.set_xlim(-2 * AU, 2 * AU)  # Define o limite do gráfico no eixo x
ax.set_ylim(-2 * AU, 2 * AU)  # Define o limite do gráfico no eixo y

# Criar os gráficos de cada corpo celeste
lines = {i: ax.plot([], [], marker="o", label=f"{body['name']}", color=body["color"], markersize=body["radius"])[0] for i, body in enumerate(bodies)}

def update(frame):
    """
    Atualiza a visualização da simulação a cada quadro da animação.

    Args:
        frame (int): O número do quadro atual

    Returns:
        list: Linhas de cada corpo celeste a serem atualizadas na animação
    """
    for i, line in lines.items():
        pos = np.array(positions[i])[:frame]  # Pega as posições até o quadro atual
        if len(pos) > 1:  # Mantém um rastro de 1 posições
            pos = pos[-1:]  # Mantém apenas as últimas 1 posições
        line.set_data(pos[:, 0], pos[:, 1])  # Atualiza a linha com o novo "rastro"
    return lines.values()

# A animação agora mostrará a simulação para 5 anos (ou o número que você definir em `num_years`)
ani = FuncAnimation(fig, update, frames=steps, interval=20, blit=True)  # Número de quadros igual ao total de dias a simular (steps)
ax.legend()
plt.show()
