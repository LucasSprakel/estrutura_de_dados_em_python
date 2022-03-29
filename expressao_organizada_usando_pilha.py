"""
Crie uma função para verificar se uma expressão composta apenas por chaves,
colchetes e parênteses, representada por uma cadeia, está ou não balanceada. Por exemplo, as expressões "[{()()}
{}]" e "{[([{}])]}" estão balanceadas, mas as expressões "{[(}])" e "{[)()(]}" não estão.

#USANDO PILHA
"""

lista = ['{', '[', '(', '[', '{', '}', ']', ')', ']', '}']
#lista = ['{', '[', ')', '(', ')', '(', ']', '}']
#lista = ['{', '[', '(', '[', '}', ']', ')', ']', '}']
#lista = ['{', '[', '(', '}', ']', ')']
#lista = ['[', '{', '(', ')', '(', ')', '}', '{', '}', ']']
#lista = ['}', '{']
i = 0
j = 0
pilha = []

while i < len(lista):
    if len(lista) % 2 != 0:
        print("Não está balanceado")
        exit(1)
    if lista[i] == '{' or lista[i] == '[' or lista[i] == '(':
        pilha.append(lista[i])
        j = j + 1
    elif lista[i] == '}' or lista[i] == ']' or lista[i] == ')':
        if len(pilha) == 0:
            print('Não está balanceado')
            exit(1)
        else:
            if lista[i] == ')' and pilha[j-1] == '(':
                pilha.pop()
                j = j - 1
            elif lista[i] == ']' and pilha[j-1] == '[':
                pilha.pop()
                j = j - 1
            elif lista[i] == '}' and pilha[j-1] == '{':
                pilha.pop()
                j = j - 1
            else:
                print('Não está balanceado')
    i = i + 1

if len(pilha) == 0:
    print('Está balanceado')
else:
    print('Não está balanceado')






