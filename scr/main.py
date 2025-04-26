from animals import DomesticAnimal, PackAnimal
from registry import Registry
from datetime import datetime

def validate_animal_type(input_type: str) -> str:
    """Проверяет и возвращает нормализованный тип животного."""
    input_type = input_type.strip().lower()
    valid_domestic = {"домашние", "дом", "д"}
    valid_pack = {"вьючные", "вьюк", "в"}
    
    while True:
        if input_type in valid_domestic:
            return "домашние"
        elif input_type in valid_pack:
            return "вьючные"
        print(f"Ошибка! '{input_type}' недопустимый тип. Используйте: домашние/вьючные.")
        input_type = input("Повторите ввод: ").strip().lower()

def validate_date(input_date: str) -> str:
    """Проверяет корректность формата даты."""
    while True:
        try:
            datetime.strptime(input_date, "%Y-%m-%d")
            return input_date
        except ValueError:
            print(f"Некорректный формат даты: '{input_date}'. Используйте ГГГГ-ММ-ДД.")
            input_date = input("Введите дату рождения: ").strip()

def main_menu():
    registry = Registry()
    
    while True:
        print("\n=== Реестр животных ===")
        print("1. Добавить животное")
        print("2. Просмотреть команды животного")
        print("3. Обучить животное новой команде")
        print("4. Показать всех животных")
        print("5. Выход")
        
        choice = input("Выберите действие: ").strip()
        
        # Добавление животного
        if choice == "1":
            try:
                name = input("Имя животного: ").strip()
                if not name:
                    raise ValueError("Имя не может быть пустым!")
                
                commands = [cmd.strip() for cmd in input("Команды (через запятую): ").split(',') if cmd.strip()]
                
                birth_date = validate_date(
                    input("Дата рождения (ГГГГ-ММ-ДД): ").strip()
                )
                
                animal_type = validate_animal_type(
                    input("Тип (домашние/вьючные): ").strip()
                )
                
                subtype = input("Подтип (например, Собака, Лошадь): ").strip()
                if not subtype:
                    raise ValueError("Подтип не может быть пустым!")
                
                # Создание объекта
                if animal_type == "домашние":
                    animal = DomesticAnimal(name, commands, birth_date, subtype)
                else:
                    animal = PackAnimal(name, commands, birth_date, subtype)
                
                registry.add_animal(animal)
                print(f"\033[92m{name} ({subtype}) успешно добавлен!\033[0m")
                
            except Exception as e:
                print(f"\033[91mОшибка: {e}\033[0m")

        # Просмотр команд
        elif choice == "2":
            name = input("Введите имя животного: ").strip()
            commands = registry.list_commands(name)
            if commands:
                print(f"Команды {name}: {', '.join(commands)}")
            else:
                print(f"\033[93mЖивотное с именем '{name}' не найдено.\033[0m")

        # Обучение команде
        elif choice == "3":
            name = input("Введите имя животного: ").strip()
            new_command = input("Введите новую команду: ").strip()
            result = registry.train_animal(name, new_command)
            print(result)

        # Показать всех животных
        elif choice == "4":
            print("\nСписок всех животных:")
            for animal in registry.animals:
                print(f"- {animal._name} ({animal._subtype}), команды: {', '.join(animal._commands)}")

        # Выход
        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("\033[93mНекорректный выбор. Попробуйте снова.\033[0m")

if __name__ == "__main__":
    main_menu()