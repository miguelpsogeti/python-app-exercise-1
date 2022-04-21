from src.Services.TodoModel import TodoModel
from datetime import datetime
import csv

class TodoUtils:
    def getTodosList(jsonString):
        todosList = list()
        for i in jsonString:
            try:
                userId = i['userId']
                id = i['id']
                title = i['title']
                completed = i['completed']
                todo = TodoModel(userId, id, title, completed)
                # Add it to the list
                todosList.append(todo)
            except:
                print("KeyError Exception")
        return todosList

    def saveTodosAsCsv(todosList):
        noProblems = True
        path = "storage\\"
        for i in todosList:
            currentDate = datetime.today().strftime('%Y-%m-%d')
            # Set row content and fileName
            fileName = i.getFileNameFormat(currentDate)
            todoContentList = i.getTodoContentListFormat()
            try:
                with open(path + fileName, 'w+', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(todoContentList)
            except:
                print(f"Exception while writing on the csv file named {fileName}")
            else:
                noProblems = False
        return noProblems

