numLeituras = int(input("Quantidade de leituras que serão realizadas no seu turno: "))
somaLeituras = 0
zonaVermelha = 0
menorLeitura = 999999
leiturasVerdes = 0
leiturasRealizadas = 0

while leiturasRealizadas < numLeituras:
    leituraAtual = int(input("Leitura(UPCs): "))
    somaLeituras += leituraAtual

    if leituraAtual < menorLeitura:
        menorLeitura = leituraAtual


    if leituraAtual >= 250:
        print("ZONA VERMELHA")
        zonaVermelha += 1
    else:
        if 120 < leituraAtual < 180:
            leiturasVerdes += 1

        zonaVermelha = 0


    if zonaVermelha >= 2:
        print("TRAVAMENTO")
        leiturasRealizadas +=1
        break
    leiturasRealizadas+=1


porcentagemVerde = (leiturasVerdes/numLeituras) * 100
relatorio = f"""
    RELATÓRIO
        Media das pressões: {somaLeituras/leiturasRealizadas:.2f}
        Menor Leitura: {menorLeitura}
        Porcentagem de leituras verdes: {porcentagemVerde:.2f}%
"""
if zonaVermelha >= 2:
    porcentagemRealizada = (leiturasRealizadas/numLeituras) * 100
    relatorio += f"        Porcentagem de leituras realizadas: {porcentagemRealizada:.2f}%"

print(relatorio)