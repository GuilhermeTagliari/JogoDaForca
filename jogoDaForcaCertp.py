# Guilherme Tagliari - 1134870
# Lorenzo Pasa - 1134869
import time
import os
def aguarde(segundos):
    time.sleep(segundos)
def limpartela():
    os.system("cls")
    
aguarde(1)
print("  ╔╗           ╔╗     ══╗")
aguarde(1)
print("  ║║           ║║   ║╔══╝")
aguarde(1)
print("  ║╠══╦══╦══╗╔═╝╠══╗║╚══╦══╦═╦══╦══╗")
aguarde(1)
print("╔╗║║╔╗║╔╗║╔╗║║╔╗║╔╗║║╔══╣╔╗║╔╣╔═╣╔╗║")
aguarde(1)
print("║╚╝║╚╝║╚╝║╚╝║║╚╝║╔╗║║║  ║╚╝║║║╚═╣╔╗║")
aguarde(1)
print("╚══╩══╩═╗╠══╝╚══╩╝╚╝╚╝  ╚══╩╝╚══╩╝╚╝")
aguarde(1)
print("      ╔═╝║")
aguarde(1)
print("      ╚══╝")
aguarde(2)
limpartela()

import os

def imprimir_opcoes_cores():
    print("Escolha a cor desejada (Número para letras e Letras para fundo):")
    print(" 0. Preto         1. Azul          2. Verde         3. Verde-água")
    print(" 4. Vermelho      5. Roxo          6. Amarelo       7. Branco")
    print(" 8. Cinza         9. Azul claro    A. Verde claro   B. Verde-água claro")
    print(" C. Vermelho claro D. Lilás        E. Amarelo claro F. Branco")

def obter_escolha_cor(mensagem):
    opcoes_validas = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', "F"]
    escolha = None
    while escolha not in opcoes_validas:
        escolha = input(mensagem).upper()
        if escolha not in opcoes_validas:
            print("Opção inválida. Tente novamente.")
    return escolha

def configurar_cores():
    limpartela()
    imprimir_opcoes_cores()
    cor_letras = obter_escolha_cor("Digite o código da cor das letras desejada: ")
    limpartela()
    imprimir_opcoes_cores()
    cor_fundo = obter_escolha_cor("Digite o código da cor de fundo desejada: ")
    limpartela()
    return cor_fundo, cor_letras

def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

cor_fundo, cor_letras = configurar_cores()
os.system(f"color {cor_letras}{cor_fundo}")
print("Cores configuradas com sucesso!")


def solicita_palavra_chave():
    while True:
        try:
            palavra_chave = input("Informe a palavra chave: ")
            if not palavra_chave.isalpha() or len(palavra_chave) < 2:
                raise ValueError
            return palavra_chave.lower()
        except ValueError:
            print("A palavra chave deve ter pelo menos 2 letras e não pode conter números ou espaços em branco.")

def solicita_dicas():
    dicas = []
    for i in range(1, 4):
        while True:
            dica = input(f"Informe a dica {i}: ")
            if dica.replace(" ", "").isalpha():
                dicas.append(dica)
                break
            else:
                print("A dica deve conter apenas caracteres alfabéticos e pode conter espaços. Tente novamente.")
    return dicas

def solicita_letra():
    letra = ""
    while len(letra) != 1:
        letra = input("Digite uma letra: ")
        if len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
    return letra.lower()

def atualiza_resposta(palavra_chave, letras_certas):
    resposta = ''
    for letra in palavra_chave:
        if letra in letras_certas:
            resposta += letra
        else:
            resposta += '_'
    return resposta

def escreve_arquivo_logs(desafiante, competidor, vencedor, palavra_chave):
    with open('jogo_da_forca_logs.txt', 'a') as arquivo:
        arquivo.write(f"Desafiante: {desafiante}, Competidor: {competidor}, Vencedor: {vencedor}, Palavra: {palavra_chave} \n")

def jogo_da_forca():
    desafiante = ""
    while not desafiante.strip():
        desafiante = input("Informe o nome do competidor: ")
    competidor = ""
    while not competidor.strip():
        competidor = input("Informe o nome do desafiante: ")
    limpartela()
    print(f"Olá, {competidor}! Seja bem-vindo(a) ao Jogo da Forca!")
    palavra_chave = solicita_palavra_chave()
    dicas = solicita_dicas()
    letras_erradas = []
    letras_certas = []
    tentativas = 0
    max_tentativas = 5
    dicas_solicitadas = 0

    while True:
        limpartela()
        resposta = atualiza_resposta(palavra_chave, letras_certas)
        print(f"Palavra chave: {resposta}")
        print(f"Letras utilizadas: {' '.join(letras_erradas + letras_certas)}")
        print(f"Erros: {len(letras_erradas)}/{max_tentativas}")
        print(f"Dicas utilizadas: {dicas_solicitadas}/3")
        desenha_forca(len(letras_erradas))

        opcao = input("Digite 1 para jogar ou 2 para solicitar uma dica: ")
        while opcao not in ['1', '2']:
            opcao = input("Digite uma opção válida (1 ou 2): ")
                
        if opcao == '2':
            if dicas_solicitadas < 3:
                print(f"Dica: {dicas[dicas_solicitadas]}")
                dicas_solicitadas += 1
            else:
                print("Você já solicitou o máximo de dicas permitido.")
                aguarde(2)
                continue
            
            letra = solicita_letra()
        else:
            letra = solicita_letra()

        if letra in letras_certas or letra in letras_erradas:
            print('Você já usou essa letra. Tente outra.')
            aguarde(2)
            continue
        elif letra in palavra_chave:
            letras_certas.append(letra)
            print("Letra correta!")
            aguarde(2)
        else:
            letras_erradas.append(letra)
            print("Letra incorreta!")
            tentativas += 1
            aguarde(2)

        if tentativas == max_tentativas:
            aguarde(2)
            print("Fim de jogo! Você atingiu o número máximo de tentativas.")
            print(f"A palavra chave era: {palavra_chave}")
            escreve_arquivo_logs(desafiante, competidor, desafiante, palavra_chave)
            desenha_forca(tentativas)
            aguarde(3)
            limpartela
            break
            
        resposta = atualiza_resposta(palavra_chave, letras_certas)
        if resposta == palavra_chave:
            limpartela()
            print(f"Parabéns, {competidor}! Você acertou a palavra chave!")
            print(f"A palavra chave era: {palavra_chave}")
            escreve_arquivo_logs(desafiante, competidor, competidor, palavra_chave)
            aguarde(3)
            limpartela
            break

def desenha_forca(tentativas):
    if tentativas == 1:
        print('  ____  ')
        print(' |    | ')
        print(' |    O ')
        print('       ')
    elif tentativas == 2:
        print('  ____  ')
        print(' |    | ')
        print(' |    O ')
        print(' |   /   ')
        print('       ')
    elif tentativas == 3:
        print('  ____  ')
        print(' |    | ')
        print(' |    O ')
        print(' |   / \ ')
        print('       ')
    elif tentativas == 4:
        print('  ____  ')
        print(' |    | ')
        print(' |    O ')
        print(' |   /|\ ')
        print(' |    |  ')
        print('       ')
    elif tentativas == 5:
        print('  ____  ')
        print(' |    | ')
        print(' |    O ')
        print(' |   /|\ ')
        print(' |    |  ')
        print(' |   / \ ')
        print('         ')
jogo_da_forca()

while True:
    try:
        opcao = input("Digite 1 para jogar novamente, 2 para sair, 3 para mostrar o histórico: ")
        if opcao not in ['1', '2', '3']:
            raise ValueError
    except ValueError:
        print("Digite uma opção válida (1, 2 ou 3)")
        continue
        
    if opcao == '1':
        aguarde(2)
        limpartela()
        jogo_da_forca()
    elif opcao == '2':
        print("Obrigado por jogar! Até a próxima!")
        aguarde(1)
        limpartela()
        break
    elif opcao == '3':
        arquivo = open("jogo_da_forca_logs.txt", "r")
        dados = arquivo.read()
        print(dados)
        arquivo.close()
        aguarde(5)
    else:
        limpartela()
        jogo_da_forca()