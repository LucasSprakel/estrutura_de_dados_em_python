class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, info):
        self.pilha.append(info)

    def desempilhar(self):
        self.pilha.pop()

    def pilha_vazia(self):
        if len(self.pilha) == 0:
            return True
        return False

    def tamanho_pilha(self):
        return len(self.pilha)

    def liberar_pilha(self):
        self.pilha.clear()


def __main__():
    #TESTES DA PILHA
    p = Pilha()

    print(p.pilha_vazia())
    print(p.tamanho_pilha())
    p.empilhar(30)
    p.empilhar(50)
    p.empilhar(100)
    print(p.pilha_vazia())
    print(p.pilha)
    p.desempilhar()
    print(p.tamanho_pilha())
    print(p.pilha)
    p.liberar_pilha()
    print(p.pilha)


__main__()
