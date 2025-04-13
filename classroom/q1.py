def main():
    print("Este programa valida um endereço IP e verifica se ele está dentro de uma faixa de endereços IPs.")

    ip = input('Digite o endereço IP: ')
    mask_start = int(input('Digite a máscara de rede inicial (CIDR): '))
    mask_end = input('Digite a máscara de rede final (CIDR)')
   
  



def to_binary(data):
    if isinstance(data, str):
        octetos = data.split('.')
        if len(octetos) != 4:
            raise ValueError("Endereço IP inválido: deve conter 4 octetos separados por pontos")
        
        binaries = []
        for octeto in octetos:
            if not octeto.isdigit():
                raise ValueError(f"Octeto inválido: '{octeto}' não é um número")
            num = int(octeto)
            if not (0 <= num <= 255):
                raise ValueError(f"Octeto inválido: {num} deve estar entre 0 e 255")
            binaries.append(format(num, '08b'))
        
        return '.'.join(binaries)

    elif isinstance(data, int):
        if not 0 <= data <= 32:
            raise ValueError("CIDR deve estar entre 0 e 32")
        mask_bin = ('1' * data).ljust(32, '0')
        octetos = [mask_bin[i:i+8] for i in range(0, 32, 8)]
        return '.'.join(octetos)

    



if __name__ == "__main__":
     main()