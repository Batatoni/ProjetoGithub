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

## Protótipo do projeto demonstrado

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

### 📌 Requisitos Funcionais

1. **Monitoramento e Classificação:** O sistema deve classificar o status operacional e prever a probabilidade de falha do AGV em tempo real.
2. **Atuação Autônoma:** O sistema deve determinar e acionar comandos virtuais automaticamente.
3. **Geração de Relatórios (LLM):** O sistema deve consumir a API do Gemini para gerar relatórios operacionais automáticos.
4. **Visualização de Métricas:** O sistema deve gerar gráficos de evolução do aprendizado de máquina.

### ⚙️ Requisitos Não-Funcionais

1. **Desempenho e Latência:** O tempo de resposta não deve ultrapassar 5 segundos.
2. **Tolerância a Falhas:** O sistema deve possuir tratamento de exceções.
3. **Confiabilidade:** O modelo deve manter acurácia superior a 90%.
4. **Escalabilidade:** O código deve ser modularizado para integração futura.

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

# 📊 7. Evidências Visuais e Desempenho

## 📉 Gráficos de Desempenho da Rede Neural

A curva de *Loss* apresentou redução progressiva até estabilização próxima de zero, enquanto a curva de *Accuracy* demonstrou excelente capacidade de generalização.

### 📊 Gráfico de Acurácia da RNA

![Evolução da Acurácia da RNA](assets/images/grafico_acuracia.png)

### 📉 Gráfico de Loss da RNA

![Evolução do Erro (Loss) da RNA](assets/images/grafico_loss.png)

### 🏗️ Fluxograma do Sistema

![Fluxograma do Sistema](assets/images/fluxograma_smartlog.png)

---

## 🤖 Log de Execução e Relatório Gemini

O sistema atua como um “co-piloto inteligente”, interpretando diagnósticos técnicos e sugerindo ações corretivas automaticamente.

```text
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
O modelo preditivo do SmartLog, com sua nova Rede Neural, demonstrou ser fundamental ao prever uma probabilidade de falha de 100.00% no AGV com base na telemetria crítica de Temperatura (108.5°C) e Vibração (5.8Hz). Essa detecção precoce e inequívoca permitiu que o sistema agisse proativamente, evitando uma quebra catastrófica que resultaria em danos extensos ao AGV, interrupções operacionais significativas e potenciais riscos de segurança. A ação do atuador de desligamento emergencial do motor e freio travado foi absolutamente adequada e crucial, pois, diante de uma certeza de falha tão elevada, essa intervenção imediata transformou uma potencial falha descontrolada em uma parada gerenciada, minimizando danos adicionais, garantindo a segurança e permitindo uma intervenção de manutenção planejada.
```

---

# 📈 8. Resultados Obtidos

O modelo demonstrou:

- Aprendizado consistente durante o treinamento;
- Excelente capacidade de generalização;
- Alta estabilidade operacional;
- Boa precisão na previsão de falhas.

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
 ┃ ┗ 📂 images
 ┣ 📂 data
 ┃ ┗ 📄 dataset
 ┣ 📂 notebooks
 ┃ ┗ 📄 Colab__SmartLog.ipynb
 ┣ 📂 scripts
 ┃ ┗ 📄 agente_previsor.py
 ┣ 📄 Requirements.txt
 ┣ 📄 README.md
```

---

# ▶️ 11. Instruções para Execução

## 1. Clone o repositório

```bash
git clone https://github.com/Batatoni/ProjetoGithub
```

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

## 3. Abra o notebook principal

Execute o arquivo `.ipynb` localizado na pasta `/notebooks`.

---

## ⚠️ Configuração da API Gemini

Adicione sua `GOOGLE_API_KEY` na aba **Secrets** do Google Colab.

---

## 4. Execute o projeto

```text
Run All
```

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

# 📚 Instituição

Centro Universitário da Fundação Santo André (FSA)  
Engenharia de Controle e Automação  
Projeto de Inteligência Artificial — 2026

---

© 2026 — SmartLog IA

