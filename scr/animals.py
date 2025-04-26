class Animal:
    def __init__(self, name, commands, birth_date):
        self._name = name
        self._commands = commands
        self._birth_date = birth_date

    def add_command(self, command):
        self._commands.append(command)

    def get_commands(self):
        return self._commands

class DomesticAnimal(Animal):
    def __init__(self, name, commands, birth_date, subtype):
        super().__init__(name, commands, birth_date)
        self._subtype = subtype  # Собака, Кошка, Хомяк

class PackAnimal(Animal):
    def __init__(self, name, commands, birth_date, subtype):
        super().__init__(name, commands, birth_date)
        self._subtype = subtype  # Лошадь, Верблюд, Осел