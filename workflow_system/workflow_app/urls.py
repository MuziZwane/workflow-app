from django.urls import path
from . import views

app_name = 'workflow_app'

urlpatterns = [
    path('customer_form/', customer_form, name='customer_form'),
    path('customer/list/', views.customer_list, name='customer_list'),
]
