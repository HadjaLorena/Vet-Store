from Model import Animal

from Model import AnimalVet

register_animal = {}

initial_id = 1

continue_loop = True

while(continue_loop == True):

  print("-=-" * 10)
  print("Menu Principal")
  print("Selecione uma das opções abaixo:")
  print("[1] Criar uma nova ficha \n[2] Acessar uma ficha já existente \n[3] Check-up do animal \n[4] Atualizar a ficha de um animal já cadastrado \n[5] Verificar o número de fichas existentes \n[6] Exibir todos os animais cadastrados \n[7] Excluir a ficha de um animal já cadastrado \n[8] Acessar a ficha de todos os animais doentes \n[9] Acessar a ficha de todos os animais saudáveis \n[10] Sair")
  vet_input = int(input("Informe sua escolha (apenas números): "))

  if(vet_input == 1):

    print("-=-" * 10)
    print("Opção 1 selecionada: CRIAR UMA NOVA FICHA")

    animal_name_input = input("Informe o nome do animal: ")
    animal_type_input = input("Informe a espécie do animal: ")
    animal_breed_input = input("Informe a raça do animal: ")
    animal_age_input = input("Informe a idade (em anos) do animal: ")

    animal = Animal(animal_name_input, animal_type_input, animal_breed_input, animal_age_input)
    animal_file = AnimalVet(initial_id, animal) # a variável já vem carregada com as informações

    register_animal.update({animal_file.id : animal_file})

    print("-=-" * 10)
    print("Animal cadastrado com sucesso!")
    print(register_animal[initial_id])

    initial_id = initial_id + 1
  
  elif(vet_input == 2):
   
    continue_loop_2 = True

    while(continue_loop_2 == True):

      print("-=-" * 10)
      print("Opção 2 selecionada: ACESSAR UMA FICHA JÁ EXISTENTE")

      vet_input = int(input("Informe o ID do animal que deseja consultar a ficha: "))

      if(vet_input > len(register_animal) or vet_input <= 0):

        print("O ID informado não consta na base de dados")
        print("Por favor, insira um ID válido")
        
        vet_input = input("Deseja pesquisar um novo animal? (SIM ou NÃO): ").lower()

        if(vet_input == "sim"):
          continue_loop_2 = True

        elif(vet_input == "não" or vet_input == "nao"):
          continue_loop_2 = False

        else:
          print("Informe uma opção válida!")

      else:
        continue_loop_2 = False
        print(register_animal[vet_input])

  elif(vet_input == 3):

    continue_loop_2 = True

    while(continue_loop_2 == True):
     
      print("-=-" * 10)
      print("Opção 3 selecionada: CHECK-UP DO ANIMAL") 

      vet_input = int(input("Informe o ID do animal: "))

      if(vet_input > len(register_animal) or vet_input <= 0):

        print("O ID informado não consta na base de dados")
        print("Por favor, insira um ID válido")

      else:
        continue_loop_2 = False
        animal_file = register_animal[vet_input]
        animal_file.check_animal_condition()

  elif(vet_input == 4):

    continue_loop_2 = True

    while(continue_loop_2 == True):

      print("-=-" * 10)
      print("Opção 4 selecionada: ATUALIZAR A FICHA DE UM ANIMAL JÁ CADASTRADO")

      vet_input = int(input("Informe o ID do animal: "))

      if(vet_input > len(register_animal) or vet_input <= 0):

        print("O ID informado não consta na base de dados")
        print("Por favor, insira um ID válido")

      else:
        continue_loop_2 = False

        animal_file = register_animal[vet_input]
        animal_file.animal.animal_update_informations()

  elif(vet_input == 5):

    print("-=-" * 10)
    print("Opção 5 selecionada: VERIFICAR O NÚMERO DE FICHAS EXISTENTES")

    number_of_files = len(register_animal)

    print(f"A quantidade de fichas cadrastradas no sistema é: {number_of_files}")

  elif(vet_input == 6):

    print("-=-" * 10)
    print("Opção 6 selecionada: EXIBIR TODOS OS ANIMAIS CADASTRADOS")

    for animal in register_animal:
      print(register_animal[animal])

  elif(vet_input == 7):

    print("-=-" * 10)
    print("Opção 7 selecionada: EXCLUIR A FICHA DE UM ANIMAL JÁ CADASTRADO")

    vet_input = int(input("Informe o ID do animal: "))

    register_animal.pop(vet_input)

  elif(vet_input == 8):

    print("-=-" * 10)
    print("Opção 8 selecionada: ACESSAR A FICHA DE TODOS OS ANIMAIS DOENTES")
    
    for animal in register_animal: #animal é o index

      if(register_animal[animal].health_condition == "O animal está doente"):
        
        print(register_animal[animal])

  elif(vet_input == 9):

    print("-=-" * 10)
    print("Opção 9 selecionada: ACESSAR A FICHA DE TODOS OS ANIMAIS SAUDÁVEIS")

    for animal in register_animal:

      if(register_animal[animal].health_condition == "O animal está saudável"):

        print(register_animal[animal])

  elif(vet_input == 10):

    print("-=-" * 10)
    print("Opção 10 selecionada: SAIR")

    continue_loop_2 = True

    while(continue_loop_2 == True):

      vet_input = input("Tem certeza que deseja sair? (SIM ou NÃO): ")

      if(vet_input == "sim"):

        continue_loop_2 = False
        continue_loop = False
        print("Até a próxima!")

      elif(vet_input == "não" or vet_input == "nao"):
        
        continue_loop_2 = False
        print("Que bom que decidiu ficar")
        print("O que deseja fazer agora?")

      else:

        print("Informe uma opção válida!")

  else:
    print("Informe uma opção válida!")