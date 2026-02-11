from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.employee_detail, name = 'employee_detail'),
    path('api/list/', views.employee_api_list, name='employee_api_list'),
]

