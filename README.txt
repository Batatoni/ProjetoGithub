1. Identificação do Grupo

Instituição: Centro Universitário da Fundação Santo André (FSA) / UNICID   

Curso: Engenharia de Controle e Automação (ECA)   

Grupo: Grupo D   

Integrantes:

Athur Salum - RA: 062220004   
Felipe Queiroz - RA: 062220020   
Thiago Frias - RA: 062220001   
Vitor Toni - RA: 062220029   
-----------------------------------------------------|
Link do Video do Pitch: https://youtu.be/GLkxSc0qg3U |
-----------------------------------------------------|
2. Área Problema Selecionada
Selecione a trilha tecnológica do projeto (marque com um [x]):

[ ] Saúde 4.0: Robótica Assistiva (Controladores Inteligentes/Fuzzy)
[ ] Smart Grid: Eficiência Energética e Descarbonização
[ ] Agtech: Automação de Precisão e Visão Computacional
[x] Logística Autônoma: Coordenação de AGVs e Otimização de Rotas   

3. Diagnóstico e Definição do Agente

Contexto: Gestão de Cadeia de Suprimentos (Supply Chain) e Transporte Logístico.   

Problema: Ineficiência na gestão das entregas e estoques, causada por rotas subotimizadas e desequilíbrio (falta ou excesso) de produtos armazenados.   

Impacto: Redução de custos operacionais, diminuição do tempo de entregas e mitigação de problemas de ruptura de estoque.   

Modelagem PEAS
Componente	Descrição
Performance (P)	
Diminuição do tempo médio de entrega, queda da taxa de atrasos e alta acurácia na previsão de falhas na frota ou demanda de estoque.

Ambiente (E)	
Malha rodoviária de entregas, frotas de veículos e centros de distribuição conectados.

Atuadores (A)	
Redefinir rotas no grafo de transporte, emitir alertas de falha, acionar LLM para relatórios de anomalias e atualizar ordens de estoque.

Sensores (S)	
Telemetria do veículo (Temperatura do Motor, Nível de Bateria e Vibração do Chassi), volume de pedidos (ERP), e APIs de trânsito.

4. Arquitetura Lógica e Aprendizado
O SmartLog opera através de uma arquitetura híbrida que garante segurança técnica e clareza para o usuário:   

Módulo Preditivo (Etapa 3): Utiliza uma Rede Neural Artificial (RNA) para identificar padrões não lineares complexos e gerar uma probabilidade contínua de falha, atuando como um sistema de aviso prévio.   

Módulo de Controle (Etapa 2): Um Sistema Especialista (Árvore de Decisão) classifica o risco com base na telemetria do veículo, que inclui a Temperatura do Motor, o Nível de Bateria e a Vibração do Chassi.   

Camada Interpretativa: A API do Gemini recebe os outputs técnicos e gera uma explicação humanizada, sugerindo ações corretivas imediatas sobre a saúde da frota.   

5. Justificativa da Abordagem
Para o desenvolvimento do núcleo de inteligência deste projeto, foi selecionada a abordagem de Redes Neurais Artificiais (RNA).   

Por que esta abordagem foi escolhida?

Natureza do Problema: O problema de otimização de frota exige uma solução que não apenas diagnostique o status atual de forma binária, mas consiga identificar padrões não lineares complexos entre a temperatura do motor, nível de bateria e vibração do chassi.   

Capacidade de Predição: A RNA foi escolhida pela sua capacidade de gerar uma probabilidade contínua de falha. Com essa previsão, o sistema funciona como um aviso prévio, permitindo aplicar lógicas graduais aos atuadores (como reduzir a velocidade em 50% em vez de uma parada brusca), mitigando o desgaste.   
+1

Escalabilidade: O modelo demonstrou aprendizado consistente ao longo de 50 epochs e atingiu excelente capacidade de generalização para garantir a segurança da frota e do estoque.   

6. Evidências Visuais e Desempenho
Arquivos armazenados na pasta /assets/images.

Imagem 1: Gráficos de Desempenho da Rede Neural Link da IMG(https://postimg.cc/RWKKdhj8)
A curva de Loss apresentou queda logarítmica até estabilizar próxima de 0, enquanto a curva de Accuracy atingiu excelente capacidade de generalização tanto nos dados de treino quanto de validação.   

Imagem 2: Log de Execução e Relatório do Gemini Link da IMG(https://postimg.cc/LY6PmThw)
O modelo atua como um "co-piloto", recebendo os diagnósticos do Sistema Especialista para gerar relatórios operacionais interpretativos e sugerir ações corretivas imediatas.   

7. Instruções para Execução
Clone o repositório: git clone [https://github.com/Batatoni/ProjetoGithub]

Instale as dependências presentes no arquivo de requisitos:   

Bash
pip install -r requirements.txt
Abra o arquivo .ipynb localizado na pasta /notebooks via Google Colab.   

Importante: Adicione sua GOOGLE_API_KEY na aba de Secrets do Colab para habilitar a camada interpretativa do LLM.   

Execute todas as células ("Run all"). O script treinará a RNA, plotará os gráficos de desempenho e consultará a API do Gemini automaticamente.   

🤖 8. Apêndice de IA
Relato sobre o suporte de ferramentas de Inteligência Artificial Generativa no desenvolvimento:

Ferramentas: Gemini 1.5 Flash / Gemini Advanced.

Aplicação: Apoio na reestruturação e modularização do código Python, implementação de princípios de Clean Code, integração da teoria dos grafos (NetworkX) e criação do roteiro de apresentação do Dashboard.

Validação: Todos os resultados, métricas de desempenho e interpretações estatísticas foram conferidos e validados tecnicamente pelo grupo.

© 2026 - Projeto de Inteligência Artificial - Centro Universitário da Fundação Santo André (FSA)
