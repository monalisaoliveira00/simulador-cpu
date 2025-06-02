Simulador de Escalonamento de Processos na CPU
Este projeto é um Simulador de Escalonamento de Processos desenvolvido em Python que implementa diferentes algoritmos clássicos de escalonamento, permitindo observar e comparar o comportamento de cada um em relação ao tempo de execução, espera e eficiência.

🎯 Objetivo

O objetivo deste simulador é fornecer uma ferramenta educacional e prática para a compreensão dos principais algoritmos de escalonamento de processos utilizados em sistemas operacionais, facilitando o aprendizado sobre como o gerenciamento de processos impacta o desempenho do sistema.

⚙️ Funcionalidades

✅ Entrada de processos com tempo de chegada e duração.
✅ Simulação de múltiplos algoritmos de escalonamento.
✅ Cálculo automático de:

Tempo de Espera

Tempo de Turnaround

Tempo de Resposta (se aplicável)
✅ Exibição clara da ordem de execução e estatísticas.
✅ Possibilidade de comparar diferentes algoritmos.

📚 Algoritmos Implementados

FCFS (First Come, First Served)
Ordem de chegada dos processos.

SJF (Shortest Job First)
Processo com a menor duração executa primeiro.

Round Robin
Processos recebem uma fatia de tempo (quantum) para execução, promovendo justiça.

Prioridade (se implementado)
Executa processos com base em prioridade definida.

🛠️ Tecnologias Utilizadas

Python 3.x — linguagem de programação.

Bibliotecas Padrão — Não há dependências externas.

🏁 Como Executar
1️⃣ Pré-requisitos
Ter o Python 3.x instalado.

Sistema operacional: Windows, Linux ou macOS.

2️⃣ Clonar o Repositório

bash
Copiar
Editar
git clone https://github.com/seu-usuario/simulador-escalonamento-cpu.git
cd simulador-escalonamento-cpu
ou apenas baixe o arquivo simulador_cpu.py.

3️⃣ Executar o Script

bash
Copiar
Editar
python simulador_cpu.py

📥 Entrada de Dados

Ao executar o script, o usuário deverá informar:

Número de processos a serem simulados.

Para cada processo:

Tempo de chegada (em unidades de tempo).

Tempo de duração (em unidades de tempo).

Prioridade (se aplicável).

Escolha do algoritmo de escalonamento.

Exemplo de entrada:

plaintext
Copiar
Editar
Digite o número de processos: 3

Processo 1 - Tempo de chegada: 0
Processo 1 - Duração: 5

Processo 2 - Tempo de chegada: 2
Processo 2 - Duração: 3

Processo 3 - Tempo de chegada: 4
Processo 3 - Duração: 1

Escolha o algoritmo:

1 - FCFS
2 - SJF
3 - Round Robin
4 - Prioridade
Se for Round Robin, o sistema pedirá também o quantum.

📊 Saída de Dados

Após a execução da simulação, o programa exibirá:

✅ Ordem de execução dos processos.
✅ Tempos individuais de espera e turnaround.
✅ Tempos médios de espera e turnaround.

Exemplo de saída:

plaintext
Copiar
Editar
Ordem de execução: P1 -> P2 -> P3

Tempo de espera:
P1: 0
P2: 3
P3: 6

Tempo médio de espera: 3.0

Tempo de turnaround:
P1: 5
P2: 6
P3: 7

Tempo médio de turnaround: 6.0

📝 Estrutura do Código

Classe Process
Representa cada processo com atributos como ID, tempo de chegada, duração, prioridade, etc.

Funções de Escalonamento
Cada algoritmo é implementado em uma função específica.

Função Principal (main)
Responsável por coletar entradas, executar o algoritmo escolhido e exibir os resultados.

✨ Exemplos de Uso

Comparar o tempo médio de espera entre FCFS e SJF para um mesmo conjunto de processos.

Analisar o impacto da variação do quantum no algoritmo Round Robin.

Observar como a prioridade altera a ordem de execução (se implementado).

🚀 Possíveis Melhorias

Implementar visualização gráfica do Gantt Chart.

Adicionar suporte para processos com tempo de bloqueio (I/O).

Implementar outros algoritmos como SRTF (Shortest Remaining Time First).

Criar uma interface gráfica (GUI) usando Tkinter ou PyQt.

 Por que usar este simulador?

✅ Simples e didático.
✅ Não depende de bibliotecas externas.
✅ Facilita o aprendizado prático sobre sistemas operacionais.
✅ Código limpo, comentado e facilmente extensível.

📄 Licença

Este projeto está licenciado sob a MIT License.
Sinta-se livre para usar, modificar e distribuir.

🤝 Contribuições

Contribuições são bem-vindas!

Abra uma issue para sugerir melhorias ou reportar bugs.

Envie um pull request com novas funcionalidades ou correções.

👤 Autor
Seu Nome
GitHub
LinkedIn

📬 Contato
Em caso de dúvidas ou sugestões, entre em contato pelo e-mail: seuemail@dominio.com.
