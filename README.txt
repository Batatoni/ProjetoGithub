# Projeto: SmartLog - Agente de Otimização Logística e Gestão de Estoque

### 1. Identificação do Grupo
* **Instituição:** Centro Universitário da Fundação Santo André (FSA) / UNICID
* **Curso:** Engenharia de Controle e Automação (ECA)
* **Grupo:** Grupo D
* **Integrantes:** 
  * [Athur Salum] - RA: [062220004]
  * [Felipe Queiroz] - RA: [062220020]
  * [Thiago Frias] - RA: [062220001]
  * [Vitor Toni] - RA: [062220029]

---

### 2. Área Problema Selecionada
Área Selecionada: Logística Autônoma: Coordenação de AGVs e Otimização de Rotas.
Contexto: Gestão de Cadeia de Suprimentos (Supply Chain) e Transporte Logístico.  
Problema: Ineficiência na gestão das entregas e estoques, causada por rotas subotimizadas e desequilíbrio (falta ou excesso) de produtos armazenados.  
Impacto: Redução de custos operacionais, diminuição do tempo de entregas e mitigação de problemas de ruptura de estoque.s

#### Modelagem PEAS
| Componente | Descrição |
| :--- | :--- |
| **Performance (P)** | Diminuição do tempo médio de entrega, queda da taxa de atrasos e alta acurácia na previsão de falhas na frota ou demanda de estoque. |
| **Ambiente (E)** | Malha rodoviária de entregas, frotas de veículos e centros de distribuição conectados. |
| **Atuadores (A)** | Redefinir rotas no grafo de transporte, emitir alertas de falha, acionar LLM para relatórios de anomalias e atualizar ordens de estoque. |
| **Sensores (S)** | Telemetria do veículo (Temperatura do Motor, Nível de Bateria e Vibração do Chassi), volume de pedidos (ERP), e APIs de trânsito. |
---

### 3. Arquitetura Lógica e Aprendizado
O SmartLog  opera através de uma arquitetura híbrida que garante segurança técnica e clareza para o usuário:  

Módulo Preditivo (Etapa 3): Utiliza uma Rede Neural Artificial (RNA) para identificar padrões não lineares complexos e gerar uma probabilidade contínua de falha, atuando como um sistema de aviso prévio.
  
Módulo de Controle (Etapa 2): Um Sistema Especialista (Árvore de Decisão) classifica o risco com base na telemetria do veículo, que inclui a Temperatura do Motor, o Nível de Bateria e a Vibração do Chassi.
  
Camada Interpretativa: A API do Gemini recebe os outputs técnicos e gera uma explicação humanizada, sugerindo ações corretivas imediatas sobre a saúde da frota. 

## Inteligência Evolutiva e Predição

### Abordagem Escolhida: Redes Neurais Artificiais (RNA)
Optamos por implementar uma **Rede Neural Artificial (RNA)** utilizando `TensorFlow/Keras`. 
* **Por quê?** Enquanto o sistema da Etapa 2 diagnosticava o status atual de forma binária (Falha/Saudável), a RNA consegue identificar padrões não lineares complexos entre a temperatura do motor, nível de bateria e vibração do chassi. Isso gera uma *probabilidade contínua de falha*, funcionando como um sistema de aviso prévio (early-warning system). Com essa previsão, podemos aplicar lógicas graduais aos atuadores (como reduzir a velocidade em 50% em vez de uma parada brusca), mitigando o desgaste antes da falha crítica acontecer.

### Métricas de Desempenho
O modelo demonstrou aprendizado consistente ao longo de 50 *epochs*. A curva de `Loss` apresentou queda logarítmica até estabilizar próxima de 0, enquanto a curva de `Accuracy` atingiu excelente capacidade de generalização tanto nos dados de treino quanto de validação.
*(Insira aqui a imagem/print dos gráficos de Loss e Accuracy gerados no Colab)*

---

### 4. Arquitetura de Dados e IA
A inteligência do agente integra as competências desenvolvidas ao longo do semestre:

* **Origem dos Dados:** Datasets simulados de características de veículos, histórico de vendas e nós de transporte.
* **Lógica de IA (Integração):**
    1. **Árvores de Decisão (`scikit-learn`):** Utilizadas para classificar a "saúde" e segurança do veículo em rota, prevendo falhas críticas com base em dados de sensores.
    2. **Redes Neurais (`tensorflow/keras`):** Implementadas para identificar padrões ocultos no histórico do ERP e prever gargalos de demanda ou probabilidade de atrasos.
    3. **Teoria dos Grafos (`networkx`):** Modela a base de conhecimento geográfico e logístico, onde os "Nós" são as cidades/CDs e as "Arestas" são os custos/tempo de transporte, permitindo cálculos de rota otimizada.
    4. **LLM (`google.generativeai`):** O modelo atuará como um "co-piloto", recebendo os diagnósticos do Sistema Especialista (Árvore de Decisão) para gerar relatórios operacionais interpretativos e sugerir ações corretivas imediatas sobre a saúde da frota de AGVs.

---

### 5. Plano de Tratamento de Dados (ETL)
1. **Extração:** Geração de matrizes de dados de simulação logística.
2. **Transformação:** Separação em dados de treino e teste, normalização de atributos numéricos e criação de matrizes de correlação para features do estoque.
3. **Carga:** Inserção estruturada nos tensores da rede neural e nos dicionários do grafo de rotas.

---

### 6. Estrutura do Repositório
* `/data`: Datasets de treino para o modelo preditivo e estrutura dos grafos logísticos.
* `/notebooks`: Arquivos `.ipynb` contendo a avaliação de performance (acurácia/loss) e plotagem das rotas.
* `/scripts`: Lógica central do agente (Agente Roteador + Agente Previsor).
* `requirements.txt`: Dependências do ambiente.
* `README.md`: Documentação atual do projeto.


---

### 7. Instruções para Execução
1. Abra o arquivo `.ipynb` localizado na pasta `/notebooks` via Google Colab.
2. Certifique-se de que a biblioteca `tensorflow` está instalada (presente no `requirements.txt`).
3. Adicione sua `GOOGLE_API_KEY` na aba de Secrets do Colab.
4. Execute todas as células ("Run all"). O script treinará a RNA, plotará os gráficos de desempenho e consultará a API do Gemini automaticamente com a previsão atualizada do atuador.
