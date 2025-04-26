from animals import DomesticAnimal, PackAnimal

class Registry:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, commands, birth_date, animal_type, subtype):
        """14.1 Завести новое животное"""
        if animal_type.lower() == "домашние":
            animal = DomesticAnimal(name, commands, birth_date, subtype)
        elif animal_type.lower() == "вьючные":
            animal = PackAnimal(name, commands, birth_date, subtype)
        else:
            raise ValueError("Некорректный тип животного")
        self.animals.append(animal)
        return f"{name} успешно добавлен!"

    def get_commands(self, name):
        """14.3 Увидеть список команд"""
        for animal in self.animals:
            if animal._name == name:
                return animal.get_commands()
        return "Животное не найдено"

    def train_animal(self, name, new_command):
        """14.4 Обучить новой команде"""
        for animal in self.animals:
            if animal._name == name:
                animal.add_command(new_command)
                return f"{name} обучен команде: {new_command}"
        return "Животное не найдено"

def main_menu():
    """14.5 Навигация по меню"""
    registry = Registry()
    while True:
        print("\n=== Реестр животных ===")
        print("1. Добавить новое животное")
        print("2. Посмотреть команды животного")
        print("3. Обучить животное новой команде")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            name = input("Имя животного: ")
            commands = input("Команды (через запятую): ").split(',')
            birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")
            animal_type = input("Тип (Домашние/Вьючные): ")
            subtype = input("Подтип (например, Собака, Лошадь): ")
            
            try:
                print(registry.add_animal(name, commands, birth_date, animal_type, subtype))
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            name = input("Введите имя животного: ")
            print(registry.get_commands(name))

        elif choice == "3":
            name = input("Введите имя животного: ")
            command = input("Введите новую команду: ")
            print(registry.train_animal(name, command))

        elif choice == "4":
            print("Выход из программы")
            break

        else:
            print("Некорректный ввод, попробуйте снова")

if __name__ == "__main__":
    main_menu()