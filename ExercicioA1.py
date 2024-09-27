import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        return f"{self.description} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"\nTarefa '{description}' adicionada com sucesso!\n")

    def list_tasks(self):
        if not self.tasks:
            print("\nNenhuma tarefa disponível.\n")
        else:
            print("\nTarefas:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
            print("")  # Espaçamento final

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print(f"\nTarefa {task_number} marcada como concluída!\n")
        else:
            print("\nNúmero da tarefa inválido!\n")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]
        print("\nTodas as tarefas concluídas foram removidas!\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    task_manager = TaskManager()

    while True:
        clear_screen()
        print("\n--- Menu de Gerenciamento de Tarefas ---")
        print("1. Adicionar nova tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefas concluídas")
        print("5. Sair")
        choice = input("\nEscolha uma opção: ")

        clear_screen()

        if choice == '1':
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
        elif choice == '2':
            task_manager.list_tasks()
            input("Pressione Enter para continuar...")  # Pausa para visualizar as tarefas
        elif choice == '3':
            task_manager.list_tasks()
            task_number = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            task_manager.mark_task_completed(task_number)
            input("Pressione Enter para continuar...")
        elif choice == '4':
            task_manager.remove_completed_tasks()
            input("Pressione Enter para continuar...")
        elif choice == '5':
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()