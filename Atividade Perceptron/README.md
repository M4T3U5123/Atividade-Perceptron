# Atividade Perceptron
# Aluno: Mateus Omar Coelho Dos Santos 

**Parâmetros Iniciais:**
- Pesos Iniciais ($w_1, w_2$): [0.0, 0.0]
- Bias Inicial ($b$): 0.0
- Taxa de Aprendizado ($\alpha$): 0.1
- Mapeamento: Sim = 1, Não = 0

## Tabela de Dados Mapeada
| Aluno | Estudou ($x_1$) | Fez o trabalho ($x_2$) | Passou ($y$) |
| :--- | :---: | :---: | :---: |
| Joãozinho | 0 | 0 | 0 |
| Huguinho | 0 | 1 | 0 |
| Zezinho | 1 | 0 | 1 |
| Luizinho | 1 | 1 | 1 |

##  Ciclo 1
###  Aluno: Joãozinho
- **Entradas**: $x_1 = 0, x_2 = 0$ | **Alvo ($y$)**: 0
- **Pesos atuais**: $w_1 = 0.00, w_2 = 0.00, b = 0.00$
- **Potencial de Ativação ($u$)**: $(0.00 \times 0) + (0.00 \times 0) + 0.00 = 0.00$
- **Predição ($\hat{y}$)**: 1 (pois $u = 0.00 \ge 0$)
- **Erro ($y - \hat{y}$)**: 0 - 1 = -1
- ** Ajuste de Pesos Necessário**:
  - $\Delta w_1 = \alpha \times erro \times x_1 = 0.1 \times -1 \times 0 = -0.00$ $\rightarrow$ $w_1 = 0.00 + (-0.00) = 0.00$
  - $\Delta w_2 = \alpha \times erro \times x_2 = 0.1 \times -1 \times 0 = -0.00$ $\rightarrow$ $w_2 = 0.00 + (-0.00) = 0.00$
  - $\Delta b = \alpha \times erro = 0.1 \times -1 = -0.10$ $\rightarrow$ $b = 0.00 + (-0.10) = -0.10$

###  Aluno: Huguinho
- **Entradas**: $x_1 = 0, x_2 = 1$ | **Alvo ($y$)**: 0
- **Pesos atuais**: $w_1 = 0.00, w_2 = 0.00, b = -0.10$
- **Potencial de Ativação ($u$)**: $(0.00 \times 0) + (0.00 \times 1) + -0.10 = -0.10$
- **Predição ($\hat{y}$)**: 0 (pois $u = -0.10 < 0$)
- **Erro ($y - \hat{y}$)**: 0 - 0 = 0
- ** Pesos Mantidos**: Não houve erro.

###  Aluno: Zezinho
- **Entradas**: $x_1 = 1, x_2 = 0$ | **Alvo ($y$)**: 1
- **Pesos atuais**: $w_1 = 0.00, w_2 = 0.00, b = -0.10$
- **Potencial de Ativação ($u$)**: $(0.00 \times 1) + (0.00 \times 0) + -0.10 = -0.10$
- **Predição ($\hat{y}$)**: 0 (pois $u = -0.10 < 0$)
- **Erro ($y - \hat{y}$)**: 1 - 0 = 1
- ** Ajuste de Pesos Necessário**:
  - $\Delta w_1 = \alpha \times erro \times x_1 = 0.1 \times 1 \times 1 = 0.10$ $\rightarrow$ $w_1 = 0.00 + (0.10) = 0.10$
  - $\Delta w_2 = \alpha \times erro \times x_2 = 0.1 \times 1 \times 0 = 0.00$ $\rightarrow$ $w_2 = 0.00 + (0.00) = 0.00$
  - $\Delta b = \alpha \times erro = 0.1 \times 1 = 0.10$ $\rightarrow$ $b = -0.10 + (0.10) = 0.00$

###  Aluno: Luizinho
- **Entradas**: $x_1 = 1, x_2 = 1$ | **Alvo ($y$)**: 1
- **Pesos atuais**: $w_1 = 0.10, w_2 = 0.00, b = 0.00$
- **Potencial de Ativação ($u$)**: $(0.10 \times 1) + (0.00 \times 1) + 0.00 = 0.10$
- **Predição ($\hat{y}$)**: 1 (pois $u = 0.10 \ge 0$)
- **Erro ($y - \hat{y}$)**: 1 - 1 = 0
- ** Pesos Mantidos**: Não houve erro.


##  Ciclo 2
###  Aluno: Joãozinho
- **Entradas**: $x_1 = 0, x_2 = 0$ | **Alvo ($y$)**: 0
- **Pesos atuais**: $w_1 = 0.10, w_2 = 0.00, b = 0.00$
- **Potencial de Ativação ($u$)**: $(0.10 \times 0) + (0.00 \times 0) + 0.00 = 0.00$
- **Predição ($\hat{y}$)**: 1 (pois $u = 0.00 \ge 0$)
- **Erro ($y - \hat{y}$)**: 0 - 1 = -1
- ** Ajuste de Pesos Necessário**:
  - $\Delta w_1 = \alpha \times erro \times x_1 = 0.1 \times -1 \times 0 = -0.00$ $\rightarrow$ $w_1 = 0.10 + (-0.00) = 0.10$
  - $\Delta w_2 = \alpha \times erro \times x_2 = 0.1 \times -1 \times 0 = -0.00$ $\rightarrow$ $w_2 = 0.00 + (-0.00) = 0.00$
  - $\Delta b = \alpha \times erro = 0.1 \times -1 = -0.10$ $\rightarrow$ $b = 0.00 + (-0.10) = -0.10$

###  Aluno: Huguinho
- **Entradas**: $x_1 = 0, x_2 = 1$ | **Alvo ($y$)**: 0
- **Pesos atuais**: $w_1 = 0.10, w_2 = 0.00, b = -0.10$
- **Potencial de Ativação ($u$)**: $(0.10 \times 0) + (0.00 \times 1) + -0.10 = -0.10$
- **Predição ($\hat{y}$)**: 0 (pois $u = -0.10 < 0$)
- **Erro ($y - \hat{y}$)**: 0 - 0 = 0
- ** Pesos Mantidos**: Não houve erro.

###  Aluno: Zezinho
- **Entradas**: $x_1 = 1, x_2 = 0$ | **Alvo ($y$)**: 1
- **Pesos atuais**: $w_1 = 0.10, w_2 = 0.00, b = -0.10$
- **Potencial de Ativação ($u$)**: $(0.10 \times 1) + (0.00 \times 0) + -0.10 = 0.00$
- **Predição ($\hat{y}$)**: 1 (pois $u = 0.00 \ge 0$)
- **Erro ($y - \hat{y}$)**: 1 - 1 = 0
- ** Pesos Mantidos**: Não houve erro.

###  Aluno: Luizinho
- **Entradas**: $x_1 = 1, x_2 = 1$ | **Alvo ($y$)**: 1
- **Pesos atuais**: $w_1 = 0.10, w_2 = 0.00, b = -0.10$
- **Potencial de Ativação ($u$)**: $(0.10 \times 1) + (0.00 \times 1) + -0.10 = 0.00$
- **Predição ($\hat{y}$)**: 1 (pois $u = 0.00 \ge 0$)
- **Erro ($y - \hat{y}$)**: 1 - 1 = 0
- ** Pesos Mantidos**: Não houve erro.
