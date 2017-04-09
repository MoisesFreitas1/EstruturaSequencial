import random

capacidadeMax = 150
pesoTotal = 245

margem1 = [50, 75, 120, 0]
margem2 = [0, 0, 0, 0]
PesoMagem2 = margem2[0]+margem2[1]+margem2[2]+margem2[3]
tentativa = 0

while PesoMagem2 < pesoTotal:
    rand1 = random.randint(0, 3)
    rand2 = random.randint(0, 3)
    while rand1 == rand2:
        rand2 = random.randint(0, 3)
    while (margem1[rand1]+margem1[rand2])>capacidadeMax:
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        while rand1 == rand2:
            rand2 = random.randint(0, 3)
    margem2[rand1] = margem1[rand1]
    margem1[rand1] = 0
    margem2[rand2] = margem1[rand2]
    margem1[rand2] = 0

    PesoMagem2 = margem2[0] + margem2[1] + margem2[2] + margem2[3]

    if PesoMagem2 < pesoTotal:
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        while rand1 == rand2:
            rand2 = random.randint(0, 3)
        while (margem2[rand1] + margem2[rand2]) > capacidadeMax:
            rand1 = random.randint(0, 3)
            rand2 = random.randint(0, 3)
            while rand1 == rand2:
                rand2 = random.randint(0, 3)
        margem1[rand1] = margem2[rand1]
        margem2[rand1] = 0
        margem1[rand2] = margem2[rand2]
        margem2[rand2] = 0

    PesoMagem2 = margem2[0] + margem2[1] + margem2[2] + margem2[3]
    tentativa = tentativa + 1

PesoMagem2 = margem2[0]+margem2[1]+margem2[2]+margem2[3]
PesoMagem1 = margem1[0]+margem1[1]+margem1[2]+margem1[3]

print("Passagem concluida no turno ",tentativa)

print(PesoMagem1," kg na margem 1")
print(PesoMagem2," kg na margem 2")
