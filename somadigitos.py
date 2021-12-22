n = int(input("Digite um número inteiro:"))
auxiliar=0
while (n != 0):
    resto = (n % 10)
    n = n// 10
    auxiliar = auxiliar + resto  
print(auxiliar)

'''
Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, 
ou seja, aquilo que é menor que o divisor; O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado,
ou seja, tudo que é maior ou igual ao divisor.
'''