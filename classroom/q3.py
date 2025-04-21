import random

RED = '\033[31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
DEFAULT = '\033[m'

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

def main(tentativas=6):
    atual = ''
    game_rules()
    sorteada = choice_word()
    atual, tentativas = validate_word(tentativas, atual, sorteada)
    compare_word(tentativas, atual, sorteada)

def compare_word(tentativas, atual, sorteada):
    if atual == sorteada:
        print(GREEN + atual + DEFAULT)
        print('Parabéns!! Você acertou a palavra!')
    elif tentativas == 0:
        print('Uma pena!!')
        print(f'A palavra sorteada foi {sorteada}!')

def get_user_input():
    try:
        return input('Digite uma palavra: ').upper()
    except KeyboardInterrupt:
        print("\nEntrada interrompida pelo usuário. Encerrando o jogo.")
        return None
    
def validate_word(tentativas, atual, sorteada):
    while (atual != sorteada) and (tentativas > 0):
        palavra = get_user_input()
        if palavra is None:
            return atual, tentativas
        if not is_valid_word(palavra):
            print("A palavra deve ter 5 letras e conter apenas caracteres alfabéticos.")
            continue
        atual = atual + '\n'
        for pos, letra in enumerate(palavra):
            if palavra == sorteada:
                atual = sorteada
                break
            elif letra == sorteada[pos]:
                atual += GREEN + letra + DEFAULT
            elif letra in sorteada:
                atual += YELLOW + letra + DEFAULT
            else:
                atual += RED + letra + DEFAULT
        tentativas -= 1
        if atual != sorteada and tentativas > 0:
            print(atual)
            print(f"Tentativas restantes: {tentativas}")
    return atual, tentativas


def is_valid_word(word):
    return len(word) == 5 and word.isalpha()

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
    return random.choice(palavras)
    

main()

