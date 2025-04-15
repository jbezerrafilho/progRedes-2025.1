import json
from datetime import datetime

def main():
    print("Este programa implementa uma calculadora de sub-redes.")
    try:
        ip = validate_ip(input('Digite o endereço IP: '))
        cidr_start = validate_cidr(input('Digite a máscara CIDR inicial: '))
        cidr_end = validate_cidr(input('Digite a máscara CIDR final: '))

        if cidr_start > cidr_end:
            raise ValueError("A máscara CIDR inicial deve ser menor ou igual à final.")

        results = {}

        for cidr in range(cidr_start, cidr_end + 1):
            network_details = calculate_network_details(ip, cidr)

            print(f"\nPara máscara /{cidr}:")
            for key, value in network_details.items():
                print(f"{key.replace('_', ' ').capitalize()}: {value}")

            results[f"/{cidr}"] = network_details

        save_to_json(results)

    except ValueError as e:
        print(f"Erro: {e}")



def validate_ip(ip):
    octetos = ip.split('.')
    if len(octetos) != 4:
        raise ValueError("Endereço IP inválido: deve conter 4 octetos separados por pontos")
    for octeto in octetos:
        if not octeto.isdigit() or not (0 <= int(octeto) <= 255):
            raise ValueError(f"Octeto inválido: '{octeto}' deve ser um número entre 0 e 255")
    return ip

def validate_cidr(cidr):
    if not cidr.isdigit():
        raise ValueError("CIDR deve ser um número inteiro")
    cidr = int(cidr)
    if not (0 <= cidr <= 32):
        raise ValueError("CIDR deve estar entre 0 e 32")
    return cidr

def ip_to_binary(ip):
    return ''.join(format(int(octeto), '08b') for octeto in ip.split('.'))

def binary_to_ip(binary_str):
    return '.'.join(str(int(binary_str[i:i+8], 2)) for i in range(0, 32, 8))

def calculate_network_details(ip, cidr):
    ip_binary = ip_to_binary(ip)
    mask_binary = ('1' * cidr).ljust(32, '0')
    mask_bin_formatted = '.'.join(mask_binary[i:i+8] for i in range(0, 32, 8))

    network_address = ''.join(
        str(int(ip_bit) & int(mask_bit)) for ip_bit, mask_bit in zip(ip_binary, mask_binary)
    )

    broadcast = network_address[:cidr] + '1' * (32 - cidr)

    first_host = network_address[:-1] + '1'
    last_host = broadcast[:-1] + '0'


    total_hosts = (2 ** (32 - cidr)) - 2

    return {
        'network_address': binary_to_ip(network_address),
        'first_host': binary_to_ip(first_host),
        'last_host': binary_to_ip(last_host),
        'broadcast': binary_to_ip(broadcast),
        'subnet_mask': binary_to_ip(mask_binary),
        'subnet_binary': mask_bin_formatted,
        'total_hosts': total_hosts
    }


def save_to_json(dados):
    # Gera nome único com timestamp
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"resultados_rede_{timestamp}.json"

    # Salva o dicionário em JSON
    with open(filename, 'w') as f:
        json.dump(dados, f, indent=4)
    print(f"\nResultados salvos no arquivo: {filename}")
    
if __name__ == "__main__":
    main()
