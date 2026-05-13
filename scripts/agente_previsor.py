import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class AgentePrevisor:
    def __init__(self):
        self.modelo = self._build_model()
        
    def _build_model(self):
        # Arquitetura baseada no Colab_(1).ipynb (16-8-1 neurônios)
        model = Sequential([
            Dense(16, activation='relu', input_shape=(3,)),
            Dense(8, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def prever_falha(self, temp, bateria, vibracao):
        dados = np.array([[temp, bateria, vibracao]])
        probabilidade = self.modelo.predict(dados, verbose=0)[0][0]
        return probabilidade

    def tomar_decisao(self, probabilidade):
        if probabilidade > 0.85:
            return "EMERGÊNCIA: Desligar AGV e travar freios."
        elif probabilidade > 0.50:
            return "ALERTA: Reduzir velocidade e desviar para manutenção."
        else:
            return "OPERACIONAL: Manter rota normal."
