from django.urls import include, path, reverse_lazy
from django.urls import path
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_protect

from .forms import CustomUserCreationForm, UserAuthenticationForm
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('orders:orders_list'),
        ),
        name='registration',
    ),
    # path('logout/', LogoutView.as_view(),
    #      name='logout'),
    path(
        'auth/login/',
        LoginView.as_view(
            template_name='registration/login.html',
            form_class=UserAuthenticationForm,
            redirect_authenticated_user=reverse_lazy('orders:orders_list'),
        ),
        name='login',
    ),
    path('profile/<int:pk>/', views.ProfileView.as_view(),
         name='profile_view'),
]
