from sys import stderr
import requests
import json
from src.Services.TodoUtils import TodoUtils


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)

        # TODO: follow README.md instructions
        r = requests.get('https://jsonplaceholder.typicode.com/todos/')
        loadedJson = json.loads(r.text)
        todosList = TodoUtils.getTodosList(loadedJson)
        TodoUtils.saveTodosAsCsv(todosList)

                
            





