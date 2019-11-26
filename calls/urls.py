# coding: UTF-8
from django.urls import path

from calls import views
from calls import cbv
from .models import Call

app_name = 'calls'

urlpatterns = [
    path('new_call/', views.call_edit, name="new_call"),
    path('new_call_customer/', views.new_call_customer, name="new_call_customer"),
    path('call_list/', views.call_list, name="call_list"),
    path('call_edit-<int:call_id>/', views.call_edit, name="call_edit"),
    path(
        'call_delete-<int:pk>/',
        cbv.CallDeleteView.as_view(


           ),
        name="call_delete"
        ),
]