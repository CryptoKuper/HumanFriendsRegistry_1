class Registry:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def list_commands(self, name):
        for animal in self._animals:
            if animal._name == name:
                return animal.get_commands()
        return "Животное не найдено."

    def train_animal(self, name, command):
        for animal in self._animals:
            if animal._name == name:
                animal.add_command(command)
                return f"{name} обучен: {command}"
        return "Животное не найдено."