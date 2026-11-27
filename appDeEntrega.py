import random
import secrets

class GeradorCodigo9Digitos:
    def __init__(self, tamanho: int = 9, usar_seguranca: bool = False):
        self.tamanho = tamanho
        self.usar_seguranca = usar_seguranca

    def gerar_inteiro(self) -> int:
        inicio = 10 ** (self.tamanho - 1)
        fim = (10 ** self.tamanho) - 1
        if self.usar_seguranca:
            return inicio + secrets.randbelow(fim - inicio + 1)
        return random.randint(inicio, fim)
#==========================================================================================#
def ler_cpf_valido() -> str:
    while True:
        documento = input("Digite o CPF para verificar o produto: ").strip()

        documento = documento.replace(".", "").replace("-", "").replace(" ", "")

        if len(documento) == 11 and documento.isdigit():
            return documento

        print("CPF inválido. Certifique-se de que o CPF tenha 11 dígitos numéricos.\n")

#==========================================================================================#
gerador = GeradorCodigo9Digitos()

documento = ler_cpf_valido()          
codigo = gerador.gerar_inteiro()      
disponibilidade = random.choice(["Disponível", "Indisponível"])

print("Código da encomenda:", codigo)
print("Disponibilidade do produto:", disponibilidade)

if disponibilidade == "Disponível":
    print("Produto disponível para entrega.")
else:
    print("Produto indisponível no momento.")