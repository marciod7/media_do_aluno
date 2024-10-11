num = float(input("1ª nota do aluno: "))
num2 = float(input("2ª nota do aluno: "))
media = (num + num2) / 2
print(f"A soma da nota de {num} + {num2} será sua média de {media:.2f}")
print("=" * 40)
if media >= 6:
    print("Parabéns. Você foi aprovada!")
elif media >= 4 and media < 6:
    print("Você está de recuperação, estude mais!")
else:
    print("Você foi reprovado!")
print("=" * 40)