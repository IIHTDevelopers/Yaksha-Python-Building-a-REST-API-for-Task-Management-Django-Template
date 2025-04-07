from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Task
from rest_framework.test import APITestCase

class TaskFunctionalTest(APITestCase):

    def test_create_task(self):
        """Test if a task is created successfully"""
        test_obj = TestUtils()
        try:
            url = '/tasks/'
            data = {
                'title': 'Test Task',
                'description': 'This is a test task.',
                'due_date': '2025-01-01T12:00:00Z',
                'status': 'To Do',
                'priority': 'Medium'
            }
            response = self.client.post(url, data, format='json')
            if response.status_code == 201 and response.data['title'] == 'Test Task':
                test_obj.yakshaAssert("TestCreateTask", True, "functional")
                print("TestCreateTask = Passed")
            else:
                test_obj.yakshaAssert("TestCreateTask", False, "functional")
                print("TestCreateTask = Failed")
        except:
            test_obj.yakshaAssert("TestCreateTask", False, "functional")
            print("TestCreateTask = Failed")

    def test_update_task(self):
        """Test if a task is updated successfully"""
        test_obj = TestUtils()
        try:
            task = Task.objects.create(
                title='Test Task', description='This is a test task.',
                due_date='2025-01-01T12:00:00Z', status='To Do', priority='Medium'
            )
            url = f'/tasks/{task.id}/'
            data = {'title': 'Updated Task'}
            response = self.client.patch(url, data, format='json')
            if response.status_code == 200 and response.data['title'] == 'Updated Task':
                test_obj.yakshaAssert("TestUpdateTask", True, "functional")
                print("TestUpdateTask = Passed")
            else:
                test_obj.yakshaAssert("TestUpdateTask", False, "functional")
                print("TestUpdateTask = Failed")
        except:
            test_obj.yakshaAssert("TestUpdateTask", False, "functional")
            print("TestUpdateTask = Failed")
