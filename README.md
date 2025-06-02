# 🧠 Simulador de CPU em Python

Este projeto é um simulador de CPU simples desenvolvido em Python. Ele interpreta e executa um conjunto reduzido de instruções similares às de uma linguagem Assembly, permitindo simular operações básicas de carregamento, armazenamento, soma e saída de dados.

## 📌 O que o projeto faz

O simulador executa instruções escritas em um arquivo `.txt` e simula o comportamento de uma CPU com registradores e memória. A cada instrução executada, o estado da CPU é exibido, incluindo o conteúdo dos registradores e posições relevantes da memória.

## 💡 Por que o projeto é útil

Este simulador é útil para entender como funciona a execução de instruções de uma CPU em nível baixo, mesmo que não seja um projeto com fins exclusivamente didáticos. Ele ajuda a visualizar conceitos como:

* Manipulação de registradores
* Acesso e modificação da memória
* Execução sequencial de instruções

Além disso, ele também pode ser usado para demonstrar o entendimento de lógica de programação e estruturas de controle.

## 🚀 Como começar a usar o projeto

### 1. Pré-requisitos

* Python 3.6 ou superior

### 2. Clone o repositório

```bash
git clone https://github.com/paulo-bento/simulador-cpu-python.git
cd simulador-cpu-python
```

### 3. Crie um arquivo de instruções (exemplo `programa_cpu.txt`)

```assembly
# Programa simples que imprime "Olá, mundo!"

PRINT "Olá, mundo!"
HLT
```

### 4. Execute o simulador com o caminho completo

```bash
python simulador_cpu.py programa_cpu.txt
```
Certifique-se de estar na mesma pasta onde os arquivos `simulador_cpu.py` e `programa_cpu.txt` estão salvos.

O simulador irá interpretar o arquivo e mostrar a execução passo a passo no terminal.

## 👥 Manutenção e contribuições

Este projeto é mantido por:

* João Paulo Bento de Lucena
* Monalisa Fernandes de Oliveira

Contribuições externas não estão abertas no momento, pois trata-se de um projeto específico para entrega acadêmica.

---

Feito com auxílio de IA generativa para o curso de Análise e Desenvolvimento de Sistemas.
