from django.urls import path , include
from .views import ShowCompView

urlpatterns = [
    path('/show/<int:genre_key>', ShowCompView.as_view())
]
