from django.urls import path

from notes import views

urlpatterns = [
    path('', views.NoteApiView.as_view(), name='notes')
]
