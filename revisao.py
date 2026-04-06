# Escreva um algoritmo que determine o número de dias que
# uma pessoa já viveu.
def ex1():
    anos = int(input("idade: "))
    meses = int(input("meses: "))
    quant_dias = (anos*365) + (meses*30)
    print(quant_dias)

# Uma empresa produz três tipos de peças mecânicas:
# parafusos, porcas e arruelas. Têm-se os preços unitários de
# cada tipo de peça e sabe-se que sobre estes preços incidem
# descontos de 10% para porcas, 20% para parafusos e 30%
# para arruelas. Escreva um algoritmo que calcule o valor
# total da compra de um cliente. Deve ser mostrado o nome
# do cliente. O número de cada tipo de peça que o mesmo
# comprou, o total de desconto e o total a pagar pela compra

def ex2():
    nome = input("Nome: ")
    parafuso = 0.02
    porca = 0.1
    arruela = 0.08
    comprap = int(input("digite quantos parafusos"))
    comprapo = int(input("digite quantas porcas"))
    compraa = int(input("digite quantas arruelas"))
    desconto = ((comprap*parafuso)-(((comprap*parafuso)/100)*20)) + ((compraa*arruela)-(((compraa*arruela)/100)*20))+ ((comprapo*porca)-(((comprapo*porca)/100)*20))
    valor_total = (((comprap*parafuso)/100)*20) + (((compraa*arruela)/100)*30) + (((comprapo*porca)/100)*10)
    print(f"valor total: {valor_total}\n" \
        f"nome: {nome}\n" \
        f"parafusos:{comprap} \n" \
        f"porcas: {comprapo}\n" \
        f"arruelas: {compraa}\n" \
        f"total de desconto: {desconto}\n")


def ex3():
    s = 0
    n = int(input("n: "))
    for i in range(n):
        soma = (3*(i+1))-1
        s += soma
    print(s)

def ex4():
    populacao = int(input("populacao"))
    sPeso = 0
    for i in range(populacao):
        peso = int(input("Peso: "))
        sPeso += peso
    mediaPeso = sPeso/populacao
    

ex4()
