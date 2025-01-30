print("Olá, vamos calcular a dose de uma QT da pediatria?")
print("Digite o peso do paciente em quilos (kg):")

while True:
    try:
        peso = float(input()) 
        if isinstance(peso, float):  
            break
        else:
            print("Por favor, insira um número válido para o peso.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

print("Digite a dose do medicamento:")

while True:
    try:
        dose = float(input())
        if isinstance(dose, float):  
            break
        else:
            print("Por favor, insira um número válido para a dose.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

if (peso <= 10 and peso > 0):
    calc_dose = (peso * dose) / 30
    print(f'Dose calculada: {calc_dose:.2f}')
else:
    sc = ((peso * 4) + 7) / (peso + 90)
    print(f'Superficie Corporal: {sc:.2f}')
    calc_dose = dose * sc
    print(f'Dose calculada: {calc_dose:.2f}')
