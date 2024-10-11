num = float(input("1ª nota do aluno: "))
num2 = float(input("2ª nota do aluno: "))
media = (num + num2) / 2
print(f"A média da nota {num} + {num2} é {media:.2f}")
if media >= 6:
    print("Parabéns. Você foi aprovada!")
else:
    print("Você foi reprovada. Estude mais!")