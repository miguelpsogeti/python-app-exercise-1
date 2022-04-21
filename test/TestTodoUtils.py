import unittest
import json
from src.Services.TodoUtils import TodoUtils

class TestTodoUtils(unittest.TestCase):

    def test_getTodosList_When1Provided_HasListLengthOf1(self):
        #setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }]'
        loadedJson = json.loads(stringifiedJson)
        todoList = TodoUtils.getTodosList(loadedJson)
        #assert
        self.assertEqual(1, len(todoList))

    def test_getTodosList_When2Provided_HasListLengthOf2(self):
        #setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }]'
        loadedJson = json.loads(stringifiedJson)
        lista = TodoUtils.getTodosList(loadedJson)
        #assert
        self.assertEqual(2, len(lista))

    def test_getTodosList_When3Provided_HasListLengthOf3(self):
        #setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }]'
        loadedJson = json.loads(stringifiedJson)
        todoList = TodoUtils.getTodosList(loadedJson)
        #assert
        self.assertEqual(3, len(todoList))

    def test_getTodosList_When4Provided_HasListLengthOf4(self):
        #setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }, { "userId": 1, "id": 4, "title": "et porro tempora", "completed": true }]'
        loadedJson = json.loads(stringifiedJson)
        todoList = TodoUtils.getTodosList(loadedJson)
        #assert
        self.assertEqual(4, len(todoList))

    def test_getTodosList_When5Provided_HasListLengthOf5(self):
        #setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }, { "userId": 1, "id": 4, "title": "et porro tempora", "completed": true }, { "userId": 1, "id": 5, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false }]'
        loadedJson = json.loads(stringifiedJson)
        todoList = TodoUtils.getTodosList(loadedJson)
        #assert
        self.assertEqual(5, len(todoList))

    def test_getTodosList_When6Provided_HasListLengthOf6(self):
        #setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }, { "userId": 1, "id": 4, "title": "et porro tempora", "completed": true }, { "userId": 1, "id": 5, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false }, { "userId": 1, "id": 6, "title": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false } ]'
        loadedJson = json.loads(stringifiedJson)
        todoList = TodoUtils.getTodosList(loadedJson)
        #assert
        self.assertEqual(6, len(todoList))

    def test_getTodosList_When6Provided_HasNotListLengthOf5(self):
        # setup
        stringifiedJson = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }, { "userId": 1, "id": 4, "title": "et porro tempora", "completed": true }, { "userId": 1, "id": 5, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false }, { "userId": 1, "id": 6, "title": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false } ]'
        loadedJson = json.loads(stringifiedJson)
        todoList = TodoUtils.getTodosList(loadedJson)
        # assert
        self.assertNotEqual(5, len(todoList))

    def test_getTodosList_When6Provided_HasNotListLengthOf7(self):
        # setup
        jsonToString = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }, { "userId": 1, "id": 4, "title": "et porro tempora", "completed": true }, { "userId": 1, "id": 5, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false }, { "userId": 1, "id": 6, "title": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false } ]'
        loadedJson = json.loads(jsonToString)
        todoList = TodoUtils.getTodosList(loadedJson)
        # assert
        self.assertNotEqual(7, len(todoList))

    def test_saveTodosAsCsv_GivenStringWithCorrectFormat_ExpectedTrue(self):
        #setup
        jsonToString = '[ { "userId": 1, "id": 1, "title": "delectus aut autem", "completed": false }, { "userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": false }, { "userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": false }, { "userId": 1, "id": 4, "title": "et porro tempora", "completed": true }, { "userId": 1, "id": 5, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum", "completed": false }, { "userId": 1, "id": 6, "title": "qui ullam ratione quibusdam voluptatem quia omnis", "completed": false } ]'
        loadedJson = json.loads(jsonToString)
        todoList = TodoUtils.getTodosList(loadedJson)
        result = TodoUtils.saveTodosAsCsv(todoList)
        #assert
        self.assertTrue(result)

