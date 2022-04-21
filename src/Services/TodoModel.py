class TodoModel:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getCompleted(self):
        return self.completed

    def setCompleted(self, newCompletedValue):
        self.completed = newCompletedValue

    def getFileNameFormat(self, date):
        result = f"{date}_{self.id}.csv"
        return result

    def getTodoContentListFormat(self):
        result = [self.userId, self.id, self.title, self.completed]
        return result