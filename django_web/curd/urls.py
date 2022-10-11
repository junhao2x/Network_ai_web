from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('chronos/performance/', views.chronos_performance, name='chronos_performance'),
    path('chronos/performance/view/', views.chronos_performance_view, name='chronos_performance_view'),
    path('chronos/accuracy/', views.chronos_accuracy, name='chronos_accuracy'),
    path('chronos/accuracy/view', views.chronos_accuracy_view, name='chronos_accuracy_view'),

]


