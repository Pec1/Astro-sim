# Astro-Sim: Simulação Gravitacional de Corpos Celestes

**Astro-Sim** é um projeto que simula o movimento de corpos celestes no sistema solar, como planetas e o Sol, utilizando as leis da gravitação universal de Newton. O projeto usa a biblioteca `matplotlib` para gerar animações dos corpos em movimento, permitindo a visualização de suas trajetórias ao longo de um período de tempo. A simulação é construída com base em cálculos de força gravitacional entre os corpos e atualização de suas posições e velocidades.

## Tecnologias Utilizadas

- **Python 3.x**
- **Numpy**: Para manipulação eficiente de vetores e cálculos matemáticos.
- **Matplotlib**: Para criação de gráficos e animações.
- **FuncAnimation (Matplotlib)**: Para animar a simulação dos corpos celestes.

## Funcionalidades

- Simulação gravitacional baseada na **Lei da Gravitação Universal** de Newton.
- Animação interativa das trajetórias dos corpos celestes, com rastro de suas posições ao longo do tempo.
- Cálculo da **força gravitacional** entre dois corpos, considerando suas massas e distâncias.
- Configuração personalizada para simulação de diferentes períodos de tempo e número de passos.

## Como Funciona

A simulação considera os seguintes corpos celestes:

- **Sol**: A estrela central do sistema.
- **Terra**: O planeta azul, com a órbita configurada em torno do Sol.
- **Marte**: O planeta vermelho, também em uma órbita simulada.

A cada passo de tempo, os corpos calculam as forças gravitacionais entre si, ajustam suas velocidades e atualizam suas posições, baseados nas equações de movimento de Newton. O código simula a movimentação desses corpos ao longo de um período de **5 anos**, com um intervalo de tempo de **1 dia**.

### Cálculos Importantes

1. **Força Gravitacional**:  
   A fórmula da força gravitacional é dada por:
   \[
   F = \frac{G \cdot m_1 \cdot m_2}{r^2}
   \]
   Onde:
   - \( G \) é a constante gravitacional (\( 6.67430 \times 10^{-11} \, m^3 \, kg^{-1} \, s^{-2} \)).
   - \( m_1 \) e \( m_2 \) são as massas dos dois corpos.
   - \( r \) é a distância entre os dois corpos.

2. **Atualização de Velocidade e Posição**:
   As velocidades dos corpos são atualizadas com base nas acelerações geradas pela força gravitacional:
   \[
   v_{i} = v_{i} + a_i \cdot \Delta t
   \]
   \[
   p_{i} = p_{i} + v_i \cdot \Delta t
   \]
   Onde:
   - \( v_i \) é a velocidade do corpo \(i\),
   - \( a_i \) é a aceleração devido à força gravitacional,
   - \( p_i \) é a posição do corpo.
