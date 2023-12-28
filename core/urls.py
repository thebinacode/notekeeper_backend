from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from core import views

urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view()),
    path('login/', obtain_auth_token, name='login'),
]
