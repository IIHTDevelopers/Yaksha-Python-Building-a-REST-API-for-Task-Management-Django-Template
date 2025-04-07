from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from library.models import Task


class TaskBoundaryTest(APITestCase):

    def test_boundary_task_list(self):
        """Test if the task list works correctly"""
        test_obj = TestUtils()
        
        try:
            Task.objects.create(
                title="test one",
                description="This is a test task.",
                due_date="2025-01-01T12:00:00Z"
            )
            Task.objects.create(
                title="test two",
                description="This is a test task.",
                due_date="2025-01-01T12:00:00Z"
            )
        except:
            test_obj.yakshaAssert("TestBoundaryTaskList", False, "boundary")
            print("TestBoundaryTaskList = Failed")
            return
        try:
            url = '/tasks/'
            response = self.client.get(url)
            if response.status_code == 200 and response.json():
                test_obj.yakshaAssert("TestBoundaryTaskList", True, "boundary")
                print("TestBoundaryTaskList = Passed")
            else:
                test_obj.yakshaAssert("TestBoundaryTaskList", False, "boundary")
                print("TestBoundaryTaskList = Failed")
        except:
            test_obj.yakshaAssert("TestBoundaryTaskList", False, "boundary")
            print("TestBoundaryTaskList = Failed")
