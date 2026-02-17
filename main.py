import colorama
import logging
import os

log_dir = "logs" 
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, "logs.log"),
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'  
)
default = False

def create_task():
    title = input("Дайте название задаче ( длина до 15 ): ")

    if len(title) > 15:
        os.system("cls")
        print(Fore.RED + "Вы превысили длину, введите название заного")
        create_task()
    else:
        with open("todo_list.txt", 'a', encoding='utf-8') as file:
            file.write(f"\nЗадача: {title} | статус: {default}")
        logging.info(f"User add task {title}")
        print(f"Задача под названием '{title}' создана, со статусом " + Fore.RED + f"{default}")

def show_task():
    try:
        with open("todo_list.txt", 'r', encoding='utf-8') as file:
            tasks = file.readlines()
            if not tasks:
                print("Список задач пуст")
                return
            
            print("\n" + "="*50)
            print("СПИСОК ЗАДАЧ:")
            for i, task in enumerate(tasks, 1):
                task = task.strip()
                if task:
                    if "статус: True" in task:
                        print(f"{i}. {task.replace('статус: True', '✅ Выполнено')}")
                    elif "статус: False" in task:
                        print(f"{i}. {task.replace('статус: False', '❌ Не выполнено')}")
                    else:
                        print(f"{i}. {task}")
            print("="*50)
    except FileNotFoundError:
        print("Файл с задачами еще не создан. Добавьте первую задачу")
    
def delete_task():
    show_task()  
    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        
        with open("todo_list.txt", 'r', encoding='utf-8') as file:
            tasks = file.readlines()
        
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks[task_num-1].strip()
            tasks.pop(task_num-1)
            
            with open("todo_list.txt", 'w', encoding='utf-8') as file:
                file.writelines(tasks)
            
            logging.info(f"User deleted task: {deleted_task}")
            print(Fore.GREEN + f"Задача '{deleted_task}' успешно удалена!")
        else:
            print(Fore.RED + "Неверный номер задачи!")
    except ValueError:
        print(Fore.RED + "Пожалуйста, введите число!")
    except FileNotFoundError:
        print("Файл с задачами не найден!")

def mark_complete():
    show_task()
    
    try:
        task_num = int(input("Введите номер задачи для отметки как выполненной: "))
        
        with open("todo_list.txt", 'r', encoding='utf-8') as file:
            tasks = file.readlines()
        
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num-1]

            if "статус: False" in task:
                updated_task = task.replace("статус: False", "статус: True")
                tasks[task_num-1] = updated_task
                
                with open("todo_list.txt", 'w', encoding='utf-8') as file:
                    file.writelines(tasks)
                
                logging.info(f"User completed task: {task.strip()}")
                print(Fore.GREEN + f"Задача отмечена как выполненная!")
            elif "статус: True" in task:
                print(Fore.YELLOW + "Эта задача уже отмечена как выполненная!")
            else:
                print(Fore.RED + "Не удалось определить статус задачи!")
        else:
            print(Fore.RED + "Неверный номер задачи!")
    except ValueError:
        print(Fore.RED + "Пожалуйста, введите число!")
    except FileNotFoundError:
        print("Файл с задачами не найден!")

def main():
    while True:
        print('Привет, выбери действие\n'
        '1. Просмотреть содержимое ToDo Листа\n'
        '2. Добавить задачу\n'
        '3. Удалить задачу\n'
        '4. Отметить задачу выполненной\n')

        userChoice = input("Я выбираю: ")

        if userChoice == '1':
            os.system('cls')
            show_task()
            input("Нажмите Enter, чтобы вернуться . . .")
            os.system('cls')
            main()
        elif userChoice == '2':
            os.system('cls')
            create_task()
            main()
        elif userChoice == '3':
            os.system('cls')
            delete_task()
        elif userChoice == '4':
            os.system('cls')
            mark_complete()
        else:
            os.system('cls')
            print("Ошибка ввода")

if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.makedirs("logs")
    main()