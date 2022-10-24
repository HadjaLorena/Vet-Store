class Animal:
  def __init__(self, animal_name, animal_type, animal_breed, animal_age):
    self.animal_name = animal_name
    self.animal_type = animal_type
    self.animal_breed = animal_breed
    self.animal_age = animal_age

  def __str__(self):
    return f"Nome: {self.animal_name} \nEspécie: {self.animal_type} \nRaça: {self.animal_breed} \nIdade: {self.animal_age} anos"

  def animal_update_informations(self):

        self.animal_name = input("Informe o nome do animal: ")
        self.animal_type = input("Informe a espécie do animal: ")
        self.animal_breed = input("Informe a raça do animal: ")
        self.animal_age = input("Informe a idade (em anos) do animal: ")