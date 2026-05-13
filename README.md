# 🚚 SmartLog IA

### Sistema Inteligente de Monitoramento Logístico e Previsão de Falhas com IA Híbrida

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)
![Status](https://img.shields.io/badge/Status-Prot%C3%B3tipo%20Funcional-blue?style=for-the-badge)

---

# 🎥 Demonstração do Projeto

## Pitch e Demonstração da Solução

https://youtu.be/GLkxSc0qg3U

## Prototipo do projeto demonstrada

https://ai.studio/apps/eb78c63e-c7c1-444d-a6bc-172e795ab2b8

---

# 📌 1. Identificação do Grupo

- **Instituição:** Centro Universitário da Fundação Santo André (FSA) / UNICID
- **Curso:** Engenharia de Controle e Automação (ECA)
- **Grupo:** Grupo D

## 👨‍💻 Integrantes

| Nome | RA |
|---|---|
| Athur Salum | 062220004 |
| Felipe Queiroz | 062220020 |
| Thiago Frias | 062220001 |
| Vitor Toni | 062220029 |

---

# 🚛 2. Área Problema Selecionada

- [ ] Saúde 4.0: Robótica Assistiva (Controladores Inteligentes/Fuzzy)
- [ ] Smart Grid: Eficiência Energética e Descarbonização
- [ ] Agtech: Automação de Precisão e Visão Computacional
- [x] **Logística Autônoma: Coordenação de AGVs e Otimização de Rotas**

---

# 🧠 3. Diagnóstico e Definição do Agente

## Contexto

O **SmartLog IA** atua no contexto de Gestão de Cadeia de Suprimentos (*Supply Chain*) e Transporte Logístico Inteligente, utilizando Inteligência Artificial para prever falhas operacionais, otimizar rotas e auxiliar no gerenciamento logístico em tempo real.

A solução integra Redes Neurais Artificiais, Sistemas Especialistas e IA Generativa para transformar dados operacionais em decisões inteligentes.

---

## Problema

Empresas logísticas enfrentam dificuldades relacionadas a:

- Rotas subotimizadas;
- Atrasos em entregas;
- Falhas inesperadas na frota;
- Desequilíbrio de estoque;
- Alto custo operacional.

Esses problemas impactam diretamente a eficiência da cadeia logística e reduzem a capacidade operacional das empresas.

---

## Impacto

A implementação do sistema permite:

- Redução do tempo médio de entrega;
- Mitigação de falhas operacionais;
- Otimização de rotas logísticas;
- Melhor distribuição de estoque;
- Maior confiabilidade operacional;
- Suporte inteligente à tomada de decisão.

---

# ⚙️ 4. Modelagem PEAS

| Componente | Descrição |
| :--- | :--- |
| **Performance (P)** | Diminuição do tempo médio de entrega, queda da taxa de atrasos e alta acurácia na previsão de falhas |
| **Environment (E)** | Malha rodoviária, frota de veículos e centros de distribuição conectados |
| **Actuators (A)** | Redefinição de rotas, emissão de alertas, atualização de estoque e geração de relatórios |
| **Sensors (S)** | Telemetria veicular, APIs de trânsito e dados de ERP |

---

# 🧬 5. Arquitetura Lógica e Aprendizado

O **SmartLog IA** utiliza uma arquitetura híbrida dividida em três camadas principais.

---

## 🔹 1. Módulo Preditivo — Rede Neural Artificial (RNA)

O sistema utiliza uma **Rede Neural Artificial** para identificar padrões complexos relacionados à saúde operacional da frota.

A RNA analisa:

- Temperatura do motor;
- Nível de bateria;
- Vibração do chassi;
- Dados operacionais históricos.

O modelo gera uma probabilidade contínua de falha, permitindo atuação preventiva antes da ocorrência de problemas críticos.

---

## 🔹 2. Módulo de Controle — Sistema Especialista

O Sistema Especialista utiliza uma **Árvore de Decisão** para classificar o risco operacional com base nos dados de telemetria.

### Exemplos:

- Temperatura elevada → Risco de superaquecimento;
- Vibração anormal → Possível falha mecânica;
- Bateria baixa → Risco operacional.

Essa camada garante rastreabilidade e confiabilidade técnica às decisões do sistema.

---

## 🔹 3. Camada Interpretativa — Gemini API

A API Gemini atua como camada interpretativa e humanizada do sistema.

### Funções da IA Generativa:

- Explicar os diagnósticos técnicos;
- Gerar relatórios operacionais;
- Sugerir ações corretivas;
- Traduzir informações complexas em linguagem acessível.

> A IA Generativa atua apenas como camada interpretativa, sem interferir diretamente na lógica determinística do Sistema Especialista.

---

## 🔹 4. Requisitos do Sistema

Para garantir a eficiência e a aplicabilidade da solução no mundo real, o **SmartLog IA** foi desenvolvido atendendo ao seguinte mapeamento de requisitos:

### 📌 Requisitos Funcionais
*(O que o sistema deve fazer)*

1. **Monitoramento e Classificação:** O sistema deve classificar o status operacional e prever a probabilidade de falha do AGV em tempo real, baseando-se nos dados de telemetria (temperatura do motor, bateria e vibração do chassi).
2. **Atuação Autônoma:** O sistema deve determinar e acionar comandos virtuais automaticamente (ex: redução de velocidade, parada emergencial) com base no nível de criticidade previsto pela Rede Neural.
3. **Geração de Relatórios (LLM):** O sistema deve consumir a API do Gemini para gerar relatórios operacionais automáticos em linguagem natural, traduzindo as anomalias dos sensores em planos de ação claros para a central de controle.
4. **Visualização de Métricas:** O sistema deve gerar gráficos de evolução do aprendizado de máquina (*Loss* e *Accuracy*) para validação do desempenho do modelo preditivo.

### ⚙️ Requisitos Não-Funcionais
*(Como o sistema deve se comportar / Restrições técnicas)*

1. **Desempenho e Latência:** O tempo de inferência e resposta para a geração do relatório via API do Gemini não deve ultrapassar 5 segundos, garantindo agilidade na tomada de decisão da central.
2. **Tolerância a Falhas:** O sistema deve possuir protocolos de contingência e tratamento de exceções (blocos *Try/Catch*). Caso a API do Gemini fique indisponível, o sistema deve manter a ação do atuador e emitir um alerta padrão de segurança.
3. **Confiabilidade:** O modelo de Rede Neural Artificial deve manter uma acurácia de validação superior a 90% para evitar falsos positivos que parem a operação logística desnecessariamente.
4. **Escalabilidade (Arquitetura):** O código deve ser modularizado de forma que o núcleo inteligente permita fácil integração futura com hardwares reais (sensores IoT de AGVs) e APIs de dashboards web.

# 🏗️ Arquitetura do Sistema

```text
Entrada de Dados
        ↓
Pré-processamento
        ↓
Rede Neural Artificial
        ↓
Previsão de Falhas
        ↓
Sistema Especialista
(Classificação de Risco)
        ↓
Gemini API
(Relatório Inteligente)
        ↓
Alertas e Recomendações
```

---

# 🤖 6. Justificativa da Abordagem

A abordagem escolhida para o núcleo inteligente do projeto foi a utilização de **Redes Neurais Artificiais (RNA)**.

---

## 🔹 Natureza do Problema

O gerenciamento logístico envolve padrões complexos e não lineares, dificultando o uso de métodos tradicionais para previsão operacional.

A RNA permite identificar relações entre múltiplas variáveis simultaneamente.

---

## 🔹 Capacidade de Predição

A RNA foi escolhida pela capacidade de prever falhas futuras antes que ocorram, funcionando como um sistema de aviso prévio inteligente.

Isso permite ações graduais como:

- Redução preventiva da velocidade;
- Replanejamento de rotas;
- Redução de desgaste operacional;
- Prevenção de paradas bruscas.

---

## 🔹 Escalabilidade

A arquitetura permite futura integração com:

- IoT;
- Sensores reais;
- Dashboards Web;
- Sistemas ERP;
- AGVs;
- Monitoramento em tempo real.

---

# 📊 7. Evidências Visuais e Desempenho

## 📉 Gráficos de Desempenho da Rede Neural

A curva de *Loss* apresentou redução progressiva até estabilização próxima de zero, enquanto a curva de *Accuracy* demonstrou excelente capacidade de generalização.

<img src="https://postimg.cc/RWKKdhj8" width="600">
![Gráfico de Desempenho da Rede Neural](https://postimg.cc/LY6PmThw)


---

## 🤖 Log de Execução e Relatório Gemini

O sistema atua como um “co-piloto inteligente”, interpretando diagnósticos técnicos e sugerindo ações corretivas automaticamente.

--- Performance do Modelo ---
Acurácia da Árvore de Decisão: 99.50%

--- Diagnóstico Operacional ---
Leitura -> Temp: 108.5°C | Bat: 22.0% | Vib: 5.8Hz
Decisão: Alerta: Falha Crítica Iminente

--- Comparação de Modelos ---
Decisão da Árvore (Etapa 2): Alerta: Falha Crítica Iminente
Probabilidade RNA (Etapa 3): 100.00% de chance de falha crítica.

Status do Atuador: ATUADOR ACIONADO: Desligamento emergencial do motor e freio travado.

--- Relatório Preditivo (Gemini API) ---
O modelo preditivo do SmartLog, com sua nova Rede Neural, demonstrou ser fundamental ao prever uma probabilidade de falha de 100.00% no AGV com base na telemetria crítica de Temperatura (108.5°C) e Vibração (5.8Hz). Essa detecção precoce e inequívoca permitiu que o sistema agisse proativamente, evitando uma quebra catastrófica que resultaria em danos extensos ao AGV, interrupções operacionais significativas e potenciais riscos de segurança. A ação do atuador de desligamento emergencial do motor e freio travado foi absolutamente adequada e crucial, pois, diante de uma certeza de falha tão elevada, essa intervenção imediata transformou uma potencial falha descontrolada em uma parada gerenciada, minimizando danos adicionais, garantindo a segurança e permitindo uma intervenção de manutenção planejada em vez de uma resposta a um colapso total do equipamento.

---

# 📈 8. Resultados Obtidos

O modelo demonstrou:

- Aprendizado consistente durante o treinamento;
- Excelente capacidade de generalização;
- Alta estabilidade operacional;
- Boa precisão na previsão de falhas.

A solução conseguiu identificar padrões relevantes de comportamento da frota e gerar respostas preventivas eficientes.

---

# 🛠️ 9. Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python | Linguagem principal |
| TensorFlow | Rede Neural Artificial |
| Scikit-Learn | Machine Learning |
| Pandas | Manipulação de dados |
| NumPy | Operações matemáticas |
| NetworkX | Modelagem de grafos |
| Gemini API | IA Generativa |
| Matplotlib | Visualização de dados |
| Google Colab | Ambiente de desenvolvimento |

---

# 📂 10. Estrutura do Repositório

```text
📦 SmartLog-IA
 ┣ 📂 assets
 ┃ ┗ 📂 images            # Gráficos de aprendizado (Loss/Accuracy) e evidências da API
 ┣ 📂 data
 ┃ ┗ 📄 dataset           # Conjunto de dados simulado de telemetria dos AGVs
 ┣ 📂 notebooks
 ┃ ┗ 📄 Colab__SmartLog.ipynb # Pipeline contínuo: Treinamento, Inferência e Integração LLM
 ┣ 📂 scripts
 ┃ ┗ 📄 agente_previsor.py    # Módulo autônomo com a lógica da Rede Neural
 ┣ 📄 Requirements.txt        # Dependências do projeto (TensorFlow, Scikit-Learn, Google Generative AI)
 ┣ 📄 README.md               # Documentação principal
```

---

# ▶️ 11. Instruções para Execução

## 1. Clone o repositório

```bash
git clone https://github.com/Batatoni/ProjetoGithub
```

---

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 3. Abra o notebook principal

Execute o arquivo `.ipynb` localizado na pasta `/notebooks` utilizando:

- Google Colab;
- Jupyter Notebook.

---

## ⚠️ Configuração da API Gemini

Adicione sua `GOOGLE_API_KEY` na aba **Secrets** do Google Colab para habilitar a camada interpretativa do sistema.

---

## 4. Execute o projeto

Selecione:

```text
Run All
```

O sistema irá:

- Treinar a RNA;
- Gerar gráficos;
- Executar a classificação;
- Consultar a API Gemini;
- Gerar relatórios automáticos.

---

# 🚀 12. Futuras Implementações

- Dashboard Web/Mobile;
- Integração IoT;
- Monitoramento em tempo real;
- Rastreamento inteligente de frota;
- Predição avançada de manutenção;
- Integração com sensores físicos;
- Coordenação de AGVs;
- Explicabilidade avançada (XAI).

---

# 🤖 13. Apêndice de IA

## Ferramentas Utilizadas

- Gemini 1.5 Flash
- Gemini Advanced
- ChatGPT

---

## Aplicação da IA

As ferramentas de IA auxiliaram em:

- Modularização do código;
- Aplicação de Clean Code;
- Integração com grafos via NetworkX;
- Estruturação da arquitetura do sistema;
- Desenvolvimento do roteiro de apresentação.

---

## Validação

Todos os resultados, métricas e interpretações foram analisados e validados tecnicamente pelo grupo.

---

# 📚 Instituição

Centro Universitário da Fundação Santo André (FSA)
Engenharia de Controle e Automação
Projeto de Inteligência Artificial — 2026

---

© 2026 — SmartLog IA

