# coding: UTF-8
from django.urls import path

from calls import views
from calls import cbv
from .models import Call

app_name = 'calls'

urlpatterns = [
    # teammember
    path('new_call/', views.call_edit, name="new_call"),
    path('call_list/', views.call_list, name="call_list"),
    path('call_list_waiting/', views.call_list_waiting, name="call_list_waiting"),
    path('call_edit-<int:call_id>/', views.call_edit, name="call_edit"),
    path('call_assign-<int:call_id>/', views.call_assign, name="call_assign"),
    path(
        'call_delete-<int:pk>/',
        cbv.CallDeleteView.as_view(),
        name="call_delete"
    ),
    # customer
    path('new_call_customer/', views.new_call_customer, name="new_call_customer"),
    path('call_list_customer/', views.call_list_customer, name="call_list_customer"),
    path('call_edit_customer-<int:call_id>/', views.call_edit_customer, name="call_edit_customer"),
]