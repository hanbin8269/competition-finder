from django.urls import path
from .views import JoinView, LoginView

urlpatterns = [
    path('/join', JoinView.as_view()),
    path('/login', LoginView.as_view()),
]