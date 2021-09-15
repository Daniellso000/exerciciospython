pontos = 4
gols = 30
contras = 0
partidas = 4
class Time():
    def mediagols(gols, partidas):
        x = gols / partidas
        return x
    def mediapontos(pontos, partidas):
        y = pontos / partidas
        return y

    def calculargols(gols, contras):
        z = gols - contras
        return z

    def atualizar():
        global gols
        global pontos
        resultado = str(input("Qual foi o resultado da partida?: "))
        if resultado == "Vitoria":
            pontos = pontos +3
        elif resultado == "Empate":
            pontos = pontos +1
        elif resultado == "Derrota":
            pontos = pontos + 0
        else:
            print("Resultado inválido")
        feitos = int(input("Quantos gols foram feitos?: "))
        sofridos = int(input("Quantos gols foram sofridos?: "))
        totalgols = gols + feitos
        totalcontras = sofridos + contras
        print(pontos, totalgols, totalcontras)

    print("Partidas:", partidas)
    print("Pontos: ", pontos)
    print("Media gols: ",mediagols(gols, partidas))
    print("Media pontos: ", mediapontos(pontos, partidas))
    print("Saldo gols: ",calculargols(gols, contras))
