import unittest
import json
from src.Services.TodoModel import TodoModel

class TestTodoModel(unittest.TestCase):
    def test_getFileNameFormat_GivenCorrectDateValue_ExpectedCorrectFilenameResult(self):
        #setup
        todo = TodoModel(1,1,"delectus aut autem",False)
        #assert
        self.assertEqual(todo.getFileNameFormat("2022-04-10"), "2022-04-10_1.csv")
    def test_getFileNameFormat_GivenIncorrectDateValue_ExpectedIncorrectFilenameResult(self):
        #setup
        todo = TodoModel(1,1,"delectus aut autem",False)
        #assert
        self.assertNotEqual(todo.getFileNameFormat(True), "2022-04-10_1.csv")
    def test_getTodoContentListFormat_GivenCorrectSetup_ExpectedEqualResult(self):
        #setup
        todo = TodoModel(1,1,"delectus aut autem",False)
        #assert
        self.assertEqual([1,1,"delectus aut autem",False], todo.getTodoContentListFormat())

    def test_getTodoContentListFormat_GivenCorrectAndDifferentExpectedOutput_ExpectedDifferentResult(self):
        #setup
        todo = TodoModel(1,1,"delectus aut autem",False)
        #assert
        self.assertNotEqual([23,27,"delectus patatum",True], todo.getTodoContentListFormat())
    def test_getUserId_GivenUserId1_ExpectingUserId1(self):
        #setup
        userId = 1
        todo = TodoModel(userId,1,"delectus aut autem",False)
        #assert
        self.assertEqual(todo.getUserId(), userId)
    def test_getUserId_GivenUserId33_NotExpectingUserId66(self):
        #setup
        userId = 33
        todo = TodoModel(userId,1,"delectus aut autem",False)
        #assert
        self.assertNotEqual(todo.getUserId(), 66)
    def test_setUserId_GivenUserId1_ExpectingUserId1(self):
        #setup
        userId = 1
        todo = TodoModel(0,1,"delectus aut autem",False)
        todo.setUserId(userId)
        #assert
        self.assertEqual(todo.getUserId(), userId)
    def test_setUserId_GivenUserId33_NotExpectingUserId66(self):
        #setup
        userId = 33
        todo = TodoModel(1,1,"delectus aut autem",False)
        todo.setUserId(userId)
        #assert
        self.assertNotEqual(todo.getUserId(), 66)
    def test_getId_GivenId3_ExpectingId3(self):
        #setup
        id = 3
        todo = TodoModel(id,1,"delectus aut autem",False)
        #assert
        self.assertEqual(todo.getUserId(), id)
    def test_getId_GivenId22_NotExpectingId44(self):
        #setup
        id = 22
        todo = TodoModel(id,1,"delectus aut autem",False)
        #assert
        self.assertNotEqual(todo.getUserId(), 44)
    def test_setId_GivenId3_ExpectingId3(self):
        #setup
        id = 3
        todo = TodoModel(1,1,"delectus aut autem",False)
        todo.setId(id)
        #assert
        self.assertEqual(todo.getId(), 3)
    def test_setId_GivenId22_NotExpectingId44(self):
        #setup
        id = 22
        todo = TodoModel(1,44,"delectus aut autem",False)
        todo.setId(id)
        #assert
        self.assertNotEqual(todo.getUserId(), 44)
    def test_getTitle_GivenValue_ExpectingSameValue(self):
        #setup
        title = "Patatum"
        todo = TodoModel(1,1,title,False)
        #assert
        self.assertEqual(todo.getTitle(), title)
    def test_getTitle_GivenValue_ExpectingDifferentValue(self):
        #setup
        title = "Patatum"
        todo = TodoModel(1,1,title,False)
        #assert
        self.assertNotEqual(todo.getTitle(), "Boniatum")
    def test_setTitle_GivenValue_ExpectingSameValue(self):
        #setup
        title = "Patatum"
        todo = TodoModel(1,1,title,False)
        newTitle = "NewPatatum"
        todo.setTitle(newTitle)
        #assert
        self.assertEqual(todo.getTitle(), newTitle)
    def test_setTitle_GivenValue_ExpectingDifferentValue(self):
        #setup
        title = "Patatum"
        todo = TodoModel(1,1,title,False)
        newTitle = "NewPatatum"
        todo.setTitle(newTitle)
        #assert
        self.assertNotEqual(todo.getTitle(), title)
    def test_getCompleted_GivenTrueValue_ExpectingTrue(self):
        #setup
        completedValue = True
        todo = TodoModel(1,1,"delectus aut autem",completedValue)
        #assert
        self.assertEqual(todo.getCompleted(), True)
    def test_getCompleted_GivenFalseValue_ExpectingFalse(self):
        #setup
        completedValue = False
        todo = TodoModel(1,1,"delectus aut autem",completedValue)
        #assert
        self.assertEqual(todo.getCompleted(), False)
    def test_getCompleted_GivenTrueValue_NotExpectingFalse(self):
        #setup
        completedValue = True
        todo = TodoModel(1,1,"delectus aut autem",completedValue)
        #assert
        self.assertNotEqual(todo.getCompleted(), False)
    def test_getCompleted_GivenFalseValue_NotExpectingTrue(self):
        #setup
        completedValue = False
        todo = TodoModel(1,1,"delectus aut autem",completedValue)
        #assert
        self.assertNotEqual(todo.getCompleted(), True)
    def test_setCompleted_GivenTrueValue_ExpectingTrue(self):
        #setup
        todo = TodoModel(1,1,"delectus aut autem",False)
        todo.setCompleted(True)
        #assert
        self.assertEqual(todo.getCompleted(), True)

    def test_setCompleted_GivenTrueValue_NotExpectingFalse(self):
        # setup
        todo = TodoModel(1, 1, "delectus aut autem", False)
        todo.setCompleted(True)
        # assert
        self.assertNotEqual(todo.getCompleted(), False)
    def test_setCompleted_GivenFalseValue_ExpectingFalse(self):
        #setup
        todo = TodoModel(1,1,"delectus aut autem",True)
        todo.setCompleted(False)
        #assert
        self.assertEqual(todo.getCompleted(), False)

    def test_setCompleted_GivenFalseValue_NotExpectingTrue(self):
        # setup
        todo = TodoModel(1, 1, "delectus aut autem", True)
        todo.setCompleted(False)
        # assert
        self.assertNotEqual(todo.getCompleted(), True)






