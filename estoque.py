class Estoque:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def retirar(self, pedido):
        if pedido <= self.quantidade:
            print("Retirada autorizada")
        else:
            print("Retirada não autorizada")

        self.quantidade -= pedido
        print("Estoque final:", self.quantidade)


estoque_inicial = int(input("Estoque disponível: "))
pedido = int(input("Quantidade solicitada: "))

estoque = Estoque(estoque_inicial)
estoque.retirar(pedido)
