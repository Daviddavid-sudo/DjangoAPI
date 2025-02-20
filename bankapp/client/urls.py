from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', views.team_view, name='profile'),
    path('profile/chat/', views.chat_view, name='chat'),
]