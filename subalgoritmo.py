def exibir_menu(d: dict) -> None:
    print("""
        -------------------------------------------------------------    
            PROGRAMA SMART SAVE (SOFTWARE DE ORGANIZAÇÃO DE FOTO)
        -------------------------------------------------------------   
            1 - Registrar nova imagem
            2 - Listar imagem
            3 - Buscar por matéria
            4 - Mostrar total
            5 - Sair
                """)

def criar_dados() -> dict:
    d ={
        "imagens": [],
        "total" : 0
    }
    return d 

def escolher_tipo() -> str:
     print("1 - Lousa")
     print("2 - Slide")
     print("3 - Anotação")
     print("4 - Fórmulas")
     print("5 - Exercícios")
     print("6 - Mapa mental")

     opcao = input("Digite o tipo: ")

     match opcao:
          case "1":
               return "Lousa"
          case "2":
               return "Slide"
          case "3":
               return "Anotação"
          case "4":
               return "Fórmulas"
          case "5":
               return "Exercícios"
          case "6":
               return "Mapa mental"
          case _:
               print("Opção invalida")

def registrar_imagem(d: dict) -> None:
    if d["total"] < 5:
        nome = input("Digite o nome da imagem: ")
        materia = input("Digite a matéria a qual a imagem se refere: ")
        tipo = escolher_tipo()

        if nome == "" or materia == "":
                print("Dados inválidos. Preencha novamente.")
        else:
            imagem = {
                 "nome":nome,    
                 "materia" : materia,            
                 "tipo" : tipo   
                 }
            d["imagens"].append(imagem)
            d["total"] = d["total"] + 1
            print("Imagem registrada com sucesso!")
    else:
        print("Limite de registros atingido.")

def listar_imagem(d: dict) -> None:
     if d["total"] == 0:
          print("Nenhuma imagem foi cadastrada.")
     else:
          for indice, imagem in enumerate(d["imagens"], start=1):
               print(f"--{indice}ª imagem ---")
               for c, v in imagem.items():
                print(f"{c}: {v}")
               print()

def buscar_materia(d: dict) -> None:
     busca = input("Digite a matéria para buscar: ")
     encontrou = False

     for imagem in d["imagens"]:
        if imagem["materia"] == busca:
             for c, v in imagem.items():
                 print(f"{c}: {v}")

def mostrar_total(d:dict) -> None:
     print(f"O total de imagens registradas é {d["total"]}")