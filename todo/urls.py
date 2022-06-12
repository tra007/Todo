from django.urls import path
from . import views

app_name = "Todo"
urlpatterns = [
    path('index/', views.homePage, name="HomePage"),
    path('info/<int:id>/', views.detail, name="DetailPage"),
    path('changeStatus/', views.changeStatus, name="ChangeStatusAjax"),
    path('deleteJob/', views.deleteJob, name="DeleteJob"),

]
