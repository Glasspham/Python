#? Tạo TODO LIST
import json
def add_task(task):
    with open('todo.json', 'r+') as file:
        tasks = json.load(file)
        tasks.append(task)
        json.dump(tasks, file)
add_task('Publish Medium article')