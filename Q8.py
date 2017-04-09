tempo = float(input("Tempo de viagem: "))
velocidade = float(input("Velocidade media: "))

distancia=tempo*velocidade
litros_usados=distancia/12

print("Velocidade Media: ", velocidade, " km/h")
print("Tempo de viagem: ", tempo, " horas")
print("Distancia percorrida: ", distancia, " km")
print("Litros de combustivel: ", litros_usados, " l")
