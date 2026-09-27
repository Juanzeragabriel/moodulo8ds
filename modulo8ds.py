excelente = 0
ruim = 0

for i in range(1, 51):

    print("\n--- ENTREVISTADO", i, "---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opinião: "))

    if opiniao == 1:
        excelente += 1

    elif opiniao == 2:
        pass

    elif opiniao == 3:
        ruim += 1

    else:
        print("Opção inválida!")

print("\n===== RESULTADO DA PESQUISA =====")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)