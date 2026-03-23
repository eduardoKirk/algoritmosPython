def ex1():
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    inter = int(input("valor: "))
    while inter >= 0:
        if inter<=25:
            cont1 += 1
        elif inter<=50:
            cont2 += 1
        elif inter<=75:
            cont3 +=1
        elif inter <=100:
            cont4 += 1
        inter = int(input("valor: "))
    print(f"[0,25]: {cont1}\n[26,50]: {cont2}\n[51,75]: {cont3}\n[76,100]: {cont4}")

def ex2():
    num = int(input("numero: "))
    while num >=0:
        if (num % 4) == 0:
            print(num)
            num -= 4
        else: 
            num -= num % 4
            print(num)

def ex3():
    a = 0
    cont = "0"
    cont2 = "0"
    while a != 10:
        num1 = int(input('valor: '))
        num2 = int(input('valor: '))
        if num1 > num2 and num1 > int(cont):
            cont2 = cont
            cont = str(num1)
        elif num2 > num1 and num2 > int(cont): 
            if num1 > int(cont):
                cont2 = num1
            elif num2 > int(cont):
                cont2 = num2
            cont = str(num2)
        a += 2
    print(cont, cont2)

# Escreva um programa que, utilizando a fórmula que converte um
# grau Fahrenheit em Celsius, imprime uma tabela com graus em
# Fahrenheit e Celsius, iniciando no grau 30 oF até 50 oF, de 2 em 2
# graus. Pesquise a fórmula na Internet

def ex4():
    F = 30
    while F <=50:
        C = (F-32) / 1.8
        print(F,C)
        F += 2

def ex5():
    num1 = 1
    num2 = 1
    S = num1/num2
    while num1 <= 98 and num2 <= 50:
        num1 += 2
        num2 += 1
        S += (num1)/(num2)
    print(S)

def ex6():
    num1 = 1
    num2 = 3
    S = num1/num2
    while num1 <= 19 and num2 <= 40:
        num1 += 1
        num2 += 2
        S += (num1)/(num2)
    print(S)
ex5()