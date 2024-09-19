from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ClientUser

# Create your views here.
def users_list(request):
    return render(request)

class ProfileView(DetailView, LoginRequiredMixin):
    template_name = 'checkout.html'
    model = ClientUser
    slug_field = 'id'
