x1 = float(input("X1: "))
y1 = float(input("Y1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

distancia = (((x2 - x1)*(x2 - x1))+((y2 - y1)*(y2 - y1)))**(1/2)

print("A distancia entre os ponto P(", x1, ",", y1, ") e Q(", x2, ",", y2, ") é: ", distancia)