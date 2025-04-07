from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import Task


class TaskExceptionalTest(APITestCase):

    def test_invalid_task_update(self):
        """Test if trying to update a non-existent task returns an error"""
        test_obj = TestUtils()
        try:
            url = '/tasks/9999/'
            data = {'title': 'Invalid Update'}
            response = self.client.patch(url, data, format='json')
            data = response.json()
            if response.status_code == 404:
                test_obj.yakshaAssert("TestInvalidTaskUpdate", True, "exceptional")
                print("TestInvalidTaskUpdate = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidTaskUpdate", False, "exceptional")
                print("TestInvalidTaskUpdate = Failed")
        except:
            test_obj.yakshaAssert("TestInvalidTaskUpdate", False, "exceptional")
            print("TestInvalidTaskUpdate = Failed")

    def test_create_task_with_invalid_due_date(self):
        """Test if creating a task with an invalid due date raises an error"""
        test_obj = TestUtils()
        try:
            url = '/tasks/'
            data = {
                'title': 'Test Task with Invalid Date',
                'description': 'This task has an invalid due date.',
                'due_date': 'Invalid Date',
                'status': 'To Do',
                'priority': 'Low'
            }
            response = self.client.post(url, data, format='json')
            if response.status_code == 400:
                test_obj.yakshaAssert("TestInvalidDueDate", True, "exceptional")
                print("TestInvalidDueDate = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidDueDate", False, "exceptional")
                print("TestInvalidDueDate = Failed")
        except:
            test_obj.yakshaAssert("TestInvalidDueDate", False, "exceptional")
            print("TestInvalidDueDate = Failed")
