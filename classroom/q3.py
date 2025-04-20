import random

RED = '\033[31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
DEFAULT = '\033[m'

def main():

    TENTATIVAS = 6
    atual = ''

    game_rules()
    sorteada = choice_word()
    atual, TENTATIVAS = validate_word(TENTATIVAS, atual, sorteada)
    if atual != sorteada and TENTATIVAS == 0:
        print('Uma pena!!')
        print(f'A palavra sorteada foi {sorteada}!')


def validate_word(TENTATIVAS, atual, sorteada):
    while (atual != sorteada) and (TENTATIVAS > 0):
        try:
            palavra = input('Digite uma palavra: ').upper()
        except KeyboardInterrupt:
            print("\nEntrada interrompida pelo usuário. Encerrando o jogo.")
            return atual, TENTATIVAS

        while len(palavra) != 5 or not palavra.isalpha():
            try:
                palavra = input('Digite uma palavra com 5 letras: ').upper()
            except KeyboardInterrupt:
                print("\nEntrada interrompida pelo usuário. Encerrando o jogo.")
                return atual, TENTATIVAS
   
        atual = atual + '\n'
        for pos in range(len(sorteada)):
            if palavra == sorteada:
                atual = sorteada
                break
            elif palavra[pos] == sorteada[pos]:
                atual = atual + GREEN + sorteada[pos] + DEFAULT         
            elif palavra[pos] in sorteada:
                atual = atual + YELLOW + palavra[pos] + DEFAULT
            else:
                atual = atual + RED + palavra[pos] + DEFAULT 
  
        compare_words(TENTATIVAS, atual, sorteada)
        
        TENTATIVAS -= 1
    return atual, TENTATIVAS

def compare_words(TENTATIVAS, atual, sorteada):
    if atual == sorteada and TENTATIVAS == 6:
        print(GREEN + atual + DEFAULT)
        print("Genial!!")
    elif atual == sorteada and TENTATIVAS == 5:
        print(GREEN + atual + DEFAULT)
        print("Fantástico!!")
    elif atual == sorteada and TENTATIVAS == 4:
        print(GREEN + atual + DEFAULT)
        print("Extraordinário!!")
    elif atual == sorteada and TENTATIVAS == 3:
        print(GREEN + atual + DEFAULT)
        print("Fenomenal!!")
    elif atual == sorteada and TENTATIVAS == 2:
        print(GREEN + atual + DEFAULT)
        print("Impressionante!!")
    elif atual == sorteada and TENTATIVAS == 1:
        print(GREEN + atual + DEFAULT)
        print("UFA!!")
    else:
        print(atual)



def game_rules():
    print(f"""
JOGO DO TERMO
Atenção às regras:
** Descubra a palavra certa. Você tem 6 tentativas!!
** Uma letra na cor {GREEN}Verde{DEFAULT} está na {GREEN}posição correta{DEFAULT} da palavra.
** Uma letra na cor {YELLOW}Amarela{DEFAULT} está {YELLOW}posiçao incorreta{DEFAULT} da palavra.
** Uma letra na cor {RED}Vermelho{DEFAULT} não faz parte da palavra.
** Podem existir letras repetidas!!
""")

def choice_word():
    palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORAL",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

    sorteada = random.choice(palavras)
    return sorteada

main()

