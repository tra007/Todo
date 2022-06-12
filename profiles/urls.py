from django.urls import path
from . import views
app_name = "User"
urlpatterns = [
    path('', views.userLogin,name="Login"),
    path('register/', views.registerUser,name="Register"),

]
