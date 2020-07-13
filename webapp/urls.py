from django.urls import path
from . import views


urlpatterns = [
    path('landing', views.landing, name="landing"),
    path('<int:user_id>', views.user_info, name="userinfo")
]