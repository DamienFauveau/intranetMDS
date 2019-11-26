from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import NewCallForm, NewCallCustomerForm, CallFormAssign
from .models import Call

def is_teammember(user=None):
    if user == None:
        return False
    return user.is_teammember

def is_customer(user=None):
    if user == None:
        return False
    return user.is_customer

@user_passes_test(is_teammember)
def call_list(request):
    calls = Call.objects.filter(teammember = request.user.teammember).order_by("-solved", "-created")
    return render(
        request,
        'calls/call_list.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_teammember)
def call_list_waiting(request):
    calls = Call.objects.filter(teammember = None).order_by("-created")
    return render(
        request,
        'calls/call_list_waiting.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_teammember)
def call_edit(request, call_id=None):
    current_instance = None
    if call_id:
        current_instance = Call.objects.get(id = call_id, teammember = request.user.teammember)
    if request.method == 'POST':
        form = NewCallForm(request.POST, instance = current_instance)
        if form.is_valid():
            if not current_instance:
                form.instance.teammember = request.user.teammember
            form.save()
    else:
        form = NewCallForm(instance = current_instance)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Appel",
            'form':form,
        }
    )

@user_passes_test(is_teammember)
def call_assign(request, call_id):
    call = Call.objects.get(id = call_id, teammember = None)
    if request.method == 'POST':
        form = CallFormAssign(request.POST, instance = call)
        if form.is_valid():
            if not call:
                form.instance.teammember = request.user.teammember
            form.save()
    else:
        form = CallFormAssign(instance = call)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Affectation d'appel",
            'form':form,
        }
    )

@user_passes_test(is_customer)
def new_call_customer(request):
    if request.method == 'POST':
        form = NewCallCustomerForm(request.POST)
        if form.is_valid():
            form.instance.customer = request.user.customer
            form.save()
    else:
        form = NewCallCustomerForm()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Nouvel Appel",
            'form':form,
        }
    )

@user_passes_test(is_customer)
def call_list_customer(request):
    calls = Call.objects.filter(customer = request.user.customer, solved = False).order_by("-created")
    return render(
        request,
        'calls/call_list_customer.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_customer)
def call_edit_customer(request, call_id):
    call = Call.objects.get(id = call_id, customer = request.user.customer, solved = False)
    if request.method == 'POST':
        form = NewCallCustomerForm(request.POST, instance = call)
        if form.is_valid():
            if not call:
                form.instance.customer = request.user.customer
            form.save()
    else:
        form = NewCallCustomerForm(instance = call)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Appel",
            'form':form,
        }
    )
