#!/usr/bin/env python3
# simulador_cpu.py - Simulador de CPU

import sys
import re

# Constantes
TAMANHO_MEMORIA = 64
REGISTRADORES_VALIDOS = {"R0", "R1", "R2"}

# Estado da CPU
memoria = [0] * TAMANHO_MEMORIA
registradores = {reg: 0 for reg in REGISTRADORES_VALIDOS}
PC = 0  # Program Counter
programa = []

def carregar_programa(nome_arquivo):
    """Carrega o programa de um arquivo .txt, ignorando comentários"""
    global programa
    try:
        with open(nome_arquivo, 'r') as f:
            for num_linha, linha in enumerate(f, 1):
                linha = linha.split('#')[0].strip()  # Remove comentários em linha
                if linha:
                    programa.append(linha)
        print(f"✓ Programa carregado: {nome_arquivo} ({len(programa)} instruções)")
    except FileNotFoundError:
        print(f"✗ Erro: Arquivo '{nome_arquivo}' não encontrado.")
        sys.exit(1)
    except IOError as e:
        print(f"✗ Erro ao ler arquivo: {str(e)}")
        sys.exit(1)

def parse_instrucao(instrucao, pc):
    """Divide a instrução em comando e operandos, respeitando strings com aspas"""
    if not instrucao:
        raise ValueError("Instrução vazia")

    # Regex que captura palavras, registradores, números e strings entre aspas
    partes = re.findall(r'".+?"|\[.*?\]|[^,\s]+', instrucao)
    comando = partes[0].upper()

    if comando in ["LOAD", "STORE", "ADD"] and len(partes) != 3:
        raise ValueError(f"Instrução {comando} requer 2 operandos")
    elif comando == "HLT" and len(partes) != 1:
        raise ValueError("HLT não requer operandos")
    elif comando == "PRINT" and len(partes) < 2:
        raise ValueError("PRINT requer ao menos um argumento")

    op1 = partes[1] if len(partes) > 1 else None
    op2 = partes[2] if len(partes) > 2 else None

    return comando, op1, op2

def executar_instrucao(instrucao, pc):
    """Executa uma única instrução com tratamento robusto de erros"""
    try:
        comando, op1, op2 = parse_instrucao(instrucao, pc)

        if comando == "LOAD":
            if op1 not in registradores:
                raise ValueError(f"Registrador inválido: {op1}")
            if op2.startswith('['):
                endereco = validar_endereco(op2[1:-1])
                valor = memoria[endereco]
            else:
                valor = validar_numero(op2)
            registradores[op1] = valor

        elif comando == "STORE":
            endereco = validar_endereco(op1.strip('[],'))
            if op2 not in registradores:
                raise ValueError(f"Registrador inválido: {op2}")
            memoria[endereco] = registradores[op2]

        elif comando == "ADD":
            if op1 not in registradores or op2 not in registradores:
                raise ValueError(f"Registradores inválidos: {op1}, {op2}")
            registradores[op1] += registradores[op2]

        elif comando == "HLT":
            return False
        
        elif comando == "PRINT":
            if not op1:
                raise ValueError("PRINT requer um operando")
            if op1.startswith('"') and op1.endswith('"'):
                print(f"\n🖨️  {op1[1:-1]}")
            elif op1 in registradores:
                print(f"\n🖨️  {registradores[op1]}")
            else:
                print(f"\n🖨️  {op1}")
        else:
            raise ValueError(f"Instrução desconhecida: {comando}")

        return True

    except Exception as e:
        print(f"\n⛔ Erro na execução (PC={pc}): {instrucao}")
        print(f"🔍 Tipo: {type(e).__name__}")
        print(f"📝 Detalhes: {str(e)}")
        return False

def validar_endereco(endereco_str):
    try:
        endereco = int(endereco_str)
        if not 0 <= endereco < TAMANHO_MEMORIA:
            raise ValueError(f"Endereço {endereco} fora dos limites (0-{TAMANHO_MEMORIA-1})")
        return endereco
    except ValueError:
        raise ValueError(f"Endereço inválido: '{endereco_str}'")

def validar_numero(num_str):
    try:
        return int(num_str)
    except ValueError:
        raise ValueError(f"Número inválido: '{num_str}'")

def mostrar_estado():
    print("\n" + "="*40)
    print("ESTADO DA CPU".center(40))
    print("="*40)
    print("\n🔹 Registradores:")
    for reg in sorted(registradores):
        print(f"  {reg}: {registradores[reg]:<10}", end="")
    print(f"\n  PC: {PC}")
    print("\n🔹 Memória (posições não nulas):")
    for i in range(0, TAMANHO_MEMORIA, 8):
        linha = [f"{i+k:02d}:{memoria[i+k]}" for k in range(8) if memoria[i+k] != 0]
        if linha:
            print("  " + " ".join(linha))
    print("="*40)

def executar_cpu():
    global PC
    print("\n" + "🚀 INICIANDO EXECUÇÃO".center(40, "="))
    while PC < len(programa):
        instrucao = programa[PC]
        print(f"\n▶ Executando (PC={PC}): {instrucao}")
        if not executar_instrucao(instrucao, PC):
            break
        PC += 1
        mostrar_estado()
    print("\n" + "🏁 EXECUÇÃO CONCLUÍDA".center(40, "="))
    mostrar_estado()

def main():
    if len(sys.argv) != 2:
        print("Uso: python simulador_cpu.py programa.txt")
        print("Exemplo: python simulador_cpu.py programa_cpu.txt")
        sys.exit(1)
    carregar_programa(sys.argv[1])
    executar_cpu()

if __name__ == "__main__":
    main()
