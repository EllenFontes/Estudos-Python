# 5.23 Leia um número e verifique se é ou não um número primo. Para fazer essa verificação,
# calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
# primos e que 2 é o único número primo que é par.

numero = int(input("Digite um número"))

inicio = 2
armazenamento = 0

while inicio < numero:
    conta = numero % inicio
    inicio += 1
    if conta == 0:
        armazenamento += 1

if numero == 0:
    print("Não é número primo")
elif numero == 1:
    print("Não é número primo")
elif armazenamento == 0:
    print("É um número primo")
else:
    print("Não é um número primo")