nome = "Joao"
idade = 16

print(nome)
print(f"O nome é {nome}")

peso = input("Digite seu peso: ")

num1 = input("Digite o primeiro numero: ")
num1 = int(num1)

num2 = int(input("Digite o segundo numero: "))

#operadores matematicos
soma = num1 + num2
sub = num - num2
multi = num1 * num2
divi = num1 / num2
divi_inteira = num1 // num2
expo = num1 ** num2
modulo = num1 % num2

# FIXME: Operadores comparativos
print("Operadores comparativos")
print(num1 > num2) # maior que
print(num1 < num2) # maior que
print(num1 == num2) # igualdade
print(num1 != num2) # diferente
print(num1 <=100) # menor ou igual

# FIXME: Operadores matematicos
print("Operadores matemáticos no print")
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

# Atribuicoes de valores
num1 += 1
num1 -= 1
num1 /= 1
num1 *= 1

print(f"Soma: {soma}")
print(f"Subtraçao: {sub}")
print(f"Multiplicaçao: {multi}")
print(f"Divisao: {divi}")
print(f"Divisao inteira: {divi_inteira}")
print(f"Divisao formatada: {divi:.2f}")
print(f"exponenciaçao: {expo}")
print(f"resto de divisao: {modulo}")
print()
print(f"O numero digitado +1 é: {num1}")
