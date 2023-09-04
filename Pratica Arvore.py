class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def inOrder(self, no):
        if no != None:
            self.inOrder(no.esquerda)
            print(no.valor, end=" ")
            self.inOrder(no.esquerda)

    def posOrder(self, no):
        if no != None:
            self.posOrder(no.esquerda)
            self.posOrder(no.esquerda)
            print(no.valor, end=" ")

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=" ")
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def altura(self, valor):
        if valor == None or valor.esquerda == None and valor.direita == None:
            return 0
        else:
            if self.altura(valor.esquerda) > self.altura(valor.direita):
                return 1 + self.altura(valor.esquerda)
            else:
                return 1 + self.altura(valor.direita)

    def mostrar_raiz(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            print("Valor da raiz:", self.raiz.valor)

    def folhas(self, valor):
        if valor == None:
            return 0
        if valor.esquerda == None and valor.direita == None:
            return 1
        return self.folhas(valor.esquerda) + self.folhas(valor.direita)

    def busca(self, chave):
        valor = self.raiz
        while valor is not None and valor.valor != chave:
            if chave < valor.valor:
                valor = valor.esquerda
            else:
                valor = valor.direita
        return valor


# Exemplo de uso
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)
print('pré-Ordem: ')
arvore.mostrar_pre_ordem()
print(' ')
print('in-Ordem: ')
arvore.inOrder(arvore.raiz)
print(' ')
print('pós-Ordem: ')
arvore.posOrder(arvore.raiz)
print('')
arvore.mostrar_raiz()
altura_arvore = arvore.altura(arvore.raiz)
print("Altura da árvore:", altura_arvore)
qtd_folhas = arvore.folhas(arvore.raiz)
print("Quantidade de folhas da árvore:", qtd_folhas)
buscarNum = int(input("Digite o número a ser procurado: "))
no_encontrado = arvore.busca(buscarNum)

if no_encontrado is not None:
    print(f"Nó {buscarNum} encontrado na árvore.")
else:
    print(f"Nó {buscarNum} não encontrado na árvore.")


