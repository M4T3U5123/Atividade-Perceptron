#ALUNO: Mateus Omar Coelho Dos Santos
#Atividade Perceptron

class PerceptronExercicio:
    def __init__(self, pesos_iniciais, taxa_aprendizagem=0.1, bias_inicial=0.0):
        self.w = list(pesos_iniciais)
        self.alpha = taxa_aprendizagem
        self.bias = bias_inicial

    def predizer(self, x):
        
        potencial = sum(xi * wi for xi, wi in zip(x, self.w)) + self.bias

        return 1 if potencial >= 0 else 0

    def treinar_exemplo(self, x, y_real):
        y_predito = self.predizer(x)
        erro = y_real - y_predito
        
      
        if erro != 0:
            self.w = [wi + self.alpha * erro * xi for xi, wi in zip(x, self.w)]
            self.bias = self.bias + self.alpha * erro
            
        return y_predito, erro


dados_treino = [
    {"aluno": "Joãozinho", "x": [0, 0], "y": 0},
    {"aluno": "Huguinho",  "x": [0, 1], "y": 0},
    {"aluno": "Zezinho",   "x": [1, 0], "y": 1},
    {"aluno": "Luizinho",  "x": [1, 1], "y": 1}
]


pesos_iniciais = [0.0, 0.0]  
taxa_aprendizado = 0.1       
bias_inicial = 0.0           


modelo = PerceptronExercicio(pesos_iniciais, taxa_aprendizado, bias_inicial)

ciclos = 2

for ciclo in range(1, ciclos + 1):
    print(f"\n--- CICLO {ciclo} ---")
    for dado in dados_treino:
        aluno = dado["aluno"]
        x = dado["x"]
        y_real = dado["y"]
        
        
        pesos_antes = list(modelo.w)
        bias_antes = modelo.bias
        
       
        y_pred, erro = modelo.treinar_exemplo(x, y_real)
        
        print(f"Aluno: {aluno.ljust(10)} | Entradas (x): {x} | Alvo (y): {y_real} | Predição: {y_pred} | Erro: {erro}")
        if erro != 0:
            print(f"   Ajuste realizado:")
            print(f"    Pesos: {pesos_antes} -> {modelo.w}")
            print(f"    Bias:  {bias_antes:.1f} -> {modelo.bias:.1f}")
        else:
            print(f"   Acertou! Pesos mantidos.")