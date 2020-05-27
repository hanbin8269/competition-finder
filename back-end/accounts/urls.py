from django.urls import path
from .views import JoinView, LoginView , UserLookupView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('/join', csrf_exempt(JoinView.as_view())),
    path('/login',csrf_exempt(LoginView.as_view())),
    path('/lookup', csrf_exempt(UserLookupView.as_view()))
]