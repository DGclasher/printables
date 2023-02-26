from .forms import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
    success_message = "Your profile has been created successfully"