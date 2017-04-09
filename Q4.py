nfuncionario = int(input("Matricula: "))
salarioAtual = float(input("Salario atual: "))
produtividade = float(input("Produtividade: "))

aumento = (salarioAtual*1.1)*(produtividade) - salarioAtual
salarioNovo = salarioAtual + aumento

print("Matricula: %d" %nfuncionario)
print("Aumento: R$ %.2f" %aumento)
print("Novo Salario: R$ %.2f" %salarioNovo)