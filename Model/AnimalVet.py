class AnimalVet:
  def __init__(self, id, animal):
    self.id = id
    self.animal = animal
    self.health_condition = "Não avaliado ainda"

  def __str__(self):
    return f"ID animal: {self.id} \n{self.animal} \nEstado de saúde: {self.health_condition}"

  def check_animal_condition(self):
    print("-=-" * 10)
    vet_check = input(f"{self.animal.animal_name} está saudável? (SIM ou NÃO): ").lower()

    if(vet_check == "sim"):
      self.health_condition = "O animal está saudável"

    elif(vet_check == "não" or vet_check == "nao"):
      self.health_condition = "O animal está doente"

    else:
      print("Insira uma informação válida!")