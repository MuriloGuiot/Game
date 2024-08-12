import random
import os
from tabela import mostrar_tabela_pontuacao


def jogar():
    """Função principal do jogo.""" 

    nome = input("Digite seu nome: ")
    numero_secreto = random.randint(1, 50)
    tentativas = 0
    limite_tentativas = 0
    pontos = 0

    print("Bem-vindo(a) ao jogo, " + nome + "! Vou pensar em um número entre 1 e 50.")

    # Seleção de dificuldade
    print("Escolha a dificuldade:")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (7 tentativas)")
    print("3 - Difícil (5 tentativas)")

    while True:
        try:
            nivel = int(input("Digite o nível de dificuldade: "))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Opção inválida. Por favor, escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Por favor, insira um número válido.")

    if nivel == 1:
        limite_tentativas = 10
    elif nivel == 2:
        limite_tentativas = 7
    else:
        limite_tentativas = 5

    print(f"Você tem {limite_tentativas} chances para adivinhar.")

    while tentativas < limite_tentativas:
        try:
            chute = int(input("Digite um número: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        tentativas += 1

        if chute < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        elif chute > numero_secreto:
            print("O número secreto é menor. Tente novamente.")
        else:
            print(f"Parabéns, {nome}! Você acertou o número secreto em {tentativas} tentativas.")
            pontos = 100  # Ganha 100 pontos por vitória
            print(f"Você ganhou {pontos} pontos!")
            return pontos, nome  # Retorna pontos e nome

    print(f"Você não conseguiu adivinhar! O número secreto era {numero_secreto}")
    return 0, nome  # Retorna 0 pontos por derrota

def main():
    """Função principal do programa."""
    tabela_pontuacao = {}  # Dicionário para armazenar pontuações dos jogadores

    while True:
        pontos, nome = jogar()
        if nome in tabela_pontuacao:
            tabela_pontuacao[nome] += pontos
        else:
            tabela_pontuacao[nome] = pontos
        mostrar_tabela_pontuacao(tabela_pontuacao)

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela no Windows ou Unix
            print("GAME OVER".center(os.get_terminal_size().columns, ' '))
            break
        

if __name__ == "__main__":
    main ()