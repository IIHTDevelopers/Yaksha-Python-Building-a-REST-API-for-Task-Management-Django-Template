from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    pass



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    pass

