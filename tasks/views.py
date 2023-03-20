from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Tasks
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status


class ListCreateTasks(ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # set the user_id to the current user's id before saving
        serializer.validated_data['user_id'] = request.user.id

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            'message': 'Task created successfully',
            'data': serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        task.delete()
        return Response({'status': 'success', 'message': 'Tasks deleted successfully'}, status=status.HTTP_200_OK)
