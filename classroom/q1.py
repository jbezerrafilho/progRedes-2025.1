
ip = input('Digite o endereço IP: ')
mask_start = input('Digite a máscara de rede inicial (CIDR)')
mask_end = input('Digite a máscara de rede final (CIDR)')

def validar_ip(ip):
    # Divide o IP em partes separadas por "."
    partes = ip.split('.')
    
    # Verifica se há exatamente 4 partes
    if len(partes) != 4:
        return False
    
    for parte in partes:
        # Verifica se cada parte é um número e está no intervalo de 0 a 255
        if not parte.isdigit() or not (0 <= int(parte) <= 255):
            return False
    
    return True

# Valida o IP
if validar_ip(ip):
    print(f'O endereço IP {ip} é válido.')
else:
    print(f'O endereço IP {ip} é inválido.')