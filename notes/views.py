from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class NoteApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({'notes': 'Hello World!'})
