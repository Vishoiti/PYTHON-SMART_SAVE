import os
os.system("cls")

from subalgoritmo import exibir_menu, criar_dados,escolher_tipo, registrar_imagem, listar_imagem, buscar_materia, mostrar_total

dicionario = criar_dados()

while True:
    exibir_menu(dicionario)
    opcao = input("Escolha: ")

    match opcao:
        case "5":
            print("O Programa terminou!.")
            break
        case "1":
            registrar_imagem(dicionario)
        case "2":
            listar_imagem(dicionario)
        case "3":
            buscar_materia(dicionario)
        case "4":
            mostrar_total(dicionario)