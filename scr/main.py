from animals import DomesticAnimal, PackAnimal
from registry import Registry

def main():
    registry = Registry()
    while True:
        print("\n1. Добавить животное\n2. Просмотреть команды\n3. Обучить\n4. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            name = input("Имя: ")
            commands = input("Команды (через запятую): ").split(",")
            birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")
            animal_type = input("Тип (Домашние/Вьючные): ").lower()
            subtype = input("Подтип: ")
            if animal_type == "домашние":
                animal = DomesticAnimal(name, commands, birth_date, subtype)
            else:
                animal = PackAnimal(name, commands, birth_date, subtype)
            registry.add_animal(animal)
            print(f"{name} добавлен!")
        elif choice == "2":
            name = input("Имя животного: ")
            print(registry.list_commands(name))
        elif choice == "3":
            name = input("Имя животного: ")
            command = input("Новая команда: ")
            print(registry.train_animal(name, command))
        elif choice == "4":
            break

if __name__ == "__main__":
    main()