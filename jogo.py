import random as rm
dicionario = open('br-utf8.txt', 'r', encoding='utf8')
leitura = dicionario.readlines()

def escolhe_palavra(leitura):
    palavra = rm.choice(leitura)
    return palavra.upper()

def play(palavra):
    completar_palavras = "_" * len(palavra)
    chute = False
    letras_chutadas = []
    palavras_chutadas = []
    tentativas = 6
    print('Vamos Jogar?')
    print("número de tentativas:", tentativas)
    print(display_hangman(tentativas))
    print(completar_palavras)
    print("\n")
    while not chute and tentativas >0:
        chutando = input("Digite uma letra").upper()
        if len(chutando) == 1 and chutando.isalpha():
            if chutando in letras_chutadas:
                print(' Você já chutou esta letra ')
                print("número de tentativas restantes:", tentativas)
            elif chutando not in palavra:
                print(chutando, "não está na palavra")
                tentativas -= 1
                letras_chutadas.append(chutando)
                print("número de tentativas restantes:", tentativas)
            else: 
                print(" Parabéns!!",chutando, "letra está na palavra ")
                #letras_chutadas.append(chutando)
                palavra_como_lista = list(completar_palavras)
                indices = [i for i, letter in enumerate(palavra) if letter == chutando]
                for indice in indices:
                    palavra_como_lista[indice] = chutando
                completar_palavras = "".join(palavra_como_lista)
                if "_" not in completar_palavras:
                    chutando = True
                print("número de tentativas restantes:", tentativas)

        elif len(chutando)== len(palavra) and chutando.isalpha():
            if chutando in palavras_chutadas:
                print (" você já chutou esta palavra ")
            elif chutando != escolhe_palavra:
                print (" Esta palavra é invalida ")
                tentativas -= 1    
            else: 
                chutando = 1
                completar_palavras = palavra
        else:
            print(" chute não valido ")
        print(display_hangman(tentativas))
        print(completar_palavras)
        print("\n")
    if chutando== True:
        print("Parabéns você adivinhou a palavra!")
    else:
        print("Você ficou sem tentativas :( a palavra era: " + palavra + ". Talvez na próxima")

def display_hangman(tentativas):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tentativas]

def jogo():
    palavra1 = escolhe_palavra(leitura)
    play(palavra1)
    while input("Jogar? [S/N]").upper() == "S":
        palavra = escolhe_palavra(leitura)
        play(palavra)

if __name__ == "__jogo__":
    jogo()

jogo()