import os

def create_note():
    note_title = input("Введите название заметки: ")
    note_content = input("Введите содержание заметки: ")

with open(f"{note_title}.txt", "w") as file:
    file.write(note_content)

print(f"Заметка '{note_title}' успешно создана!")

def display_notes():
notes = [f for f in os.listdir() if f.endswith('.txt')]

if notes:
    print("Ваши заметки:")
for note in notes:
    print(f"- {note[:-4]}") # Убираем .txt для удобства
else:
    print("У вас нет созданных заметок.")

def edit_note():
note_title = input("Введите название заметки для редактирования: ")

if os.path.exists(f"{note_title}.txt"):
    with open(f"{note_title}.txt", "r") as file:
        content = file.read()
print(f"Содержимое заметки:\n{content}")

new_content = input("Введите новое содержание заметки: ")

with open(f"{note_title}.txt", "w") as file:
file.write(new_content)

print(f"Заметка '{note_title}' успешно обновлена!")
else:
print("Заметка не найдена.")

def delete_note():
    note_title = input("Введите название заметки для удаления: ")

if os.path.exists(f"{note_title}.txt"):
    os.remove(f"{note_title}.txt")
    print(f"Заметка '{note_title}' успешно удалена!")
else:
print("Заметка не найдена.")
def main_menu():
while True:
    print("\n--- Меню системы заметок ---")
    print("1. Создать заметку")
    print("2. Отобразить заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

choice = input("Выберите опцию (1-5): ")

if choice == "1":
    create_note()
elif choice == "2":
    display_notes()
elif choice == "3":
    edit_note()
elif choice == "4":
    delete_note()
elif choice == "5":
    print("Выход из программы.")
break
else:
print("Неверный ввод. Пожалуйста, попробуйте снова.")

def main():
main_menu()

if __name__ == "__main__":
main()

