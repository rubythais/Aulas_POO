import ipaddress

class Rede:
    def __init__(self, ip: str, mascara: int):
        self.ip = self.validar_ip(ip)
        self.mascara = self.validar_mascara(mascara)
        self.rede = self.calcular_rede()

    @staticmethod
    def validar_ip(ip: str) -> str:
        try:
            ipaddress.IPv4Address(ip) 
            return ip
        except ipaddress.AddressValueError:
            raise ValueError(f"'{ip}' não é um endereço IP válido.")

    @staticmethod
    def validar_mascara(mascara: int) -> int: 
        if 1 <= mascara <= 32:
            return mascara
        else:
            raise ValueError(f"'{mascara}' não é uma máscara válida. Deve ser entre 1 e 32.")

    def calcular_rede(self):
        try:
            return ipaddress.IPv4Network(f"{self.ip}/{self.mascara}", strict=False)
        except ValueError as e:
            raise ValueError(f"Erro ao calcular a rede: {e}")

    def mesma_rede(self, outra_rede) -> bool: 
        return self.rede.network_address == outra_rede.rede.network_address

def entradas():
    while True:
        try:
            ip = input("Digite o IP (ex.: 000.000.0.00): ")
            mascara = int(input("Digite a máscara de sub-rede (1-32): "))
            return Rede(ip, mascara)
        except ValueError as e:
            print(f"Entrada inválida: {e}")
          

if __name__ == "__main__":
    print("Entre com os dados da primeira rede:")
    rede1 = entradas()

    print("\nEntre com os dados da segunda rede:")
    rede2 = entradas()

    if rede1.mesma_rede(rede2):
        print("\nVerdadeiro")
    else:
        print("\nFalso")
