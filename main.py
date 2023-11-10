class Human:
    def __init__(self, name):
        self.name = name

    def interact_with_pet(self, pet):
        print(f"{self.name} взаємодіє з {pet.species} по імені {pet.name}")
        pet.feed()
        pet.play()

class Pet:


human = Human("Олександр")
my_pet = Pet("Барсік", "Кіт")

human.interact_with_pet(my_pet)
print(f"{my_pet.name} щастливість: {my_pet.happiness}")