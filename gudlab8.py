from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Task:
    id: int
    name: str
    description: str
    status: str


@dataclass
class TaskManager:
    tasks: List[Task]

    def add_task(self, task: Task) -> 'TaskManager':
        new_tasks = self.tasks[:]
        new_tasks.append(task)
        return TaskManager(new_tasks)

    def complete_task(self, task_id: int) -> 'TaskManager':
        new_tasks = [task if task.id != task_id else Task(task.id, task.name, task.description, 'completed') for task in self.tasks]
        return TaskManager(new_tasks)

    def get_tasks_by_status(self, status: str) -> List[Task]:
        return [task for task in self.tasks if task.status == status]


# Пример использования
if __name__ == "__main__":
    initial_tasks = []
    task_manager = TaskManager(initial_tasks)

    # Добавление задач
    task_manager = task_manager.add_task(Task(1, "Покупки", "Купить продукты в магазине", "todo"))
    task_manager = task_manager.add_task(Task(2, "Уборка", "Провести уборку в квартире", "todo"))
    task_manager = task_manager.add_task(Task(3, "Прогулка", "Прогуляться в парке", "in_progress"))

    # Пометка задачи как завершенной
    task_manager = task_manager.complete_task(1)

    # Получение задач по статусу
    tasks_in_progress = task_manager.get_tasks_by_status("in_progress")
    print("Задачи в процессе выполнения:", tasks_in_progress)
