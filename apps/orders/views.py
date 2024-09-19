from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Product, Categories
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib import messages
import random

from . forms import  ProductCreateForm, MailingEmailForm


class ProductListView(ListView):
    model = Product
    template_name = 'shop.html'  # Настройка шаблона
    paginate_by = 6

    def get_queryset(self) -> QuerySet[Any]:
        model = Product.objects.all()[::-1]
        return model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        try: 
            context['products'] = random.sample(list(Product.objects.all()), 5) 
        except: 
            context['products'] = Product.objects.all()
        # Add any additional context variables here
        return context


# Детали продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['products'] = random.sample(list(Product.objects.all()), 5) 
        except: 
            context['products'] = Product.objects.all() 
        # You can add additional data to the context here if needed
        return context


# Создание продукта
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'single-post.html'  # Настройка шаблона
    success_url = '/products/'  # Куда перенаправлять после успешного создания

# Обновление продукта
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product_form.html'
    success_url = '/products/'

# Удаление продукта
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = '/products/'

# Create your views here.
def orders_list(request):
    context = {}
    products = random.sample(list(Product.objects.all()), 5)
    product_last = Product.objects.all()[:3]
    context = {
        'product_last': product_last,
        'products': products,
    }
    return render(request, 'index.html', context)


def about_view(request):
    context = {}
    try: 
        context['products'] = random.sample(list(Product.objects.all()), 5) 
    except: 
        context['products'] = Product.objects.all() 
    return render(request, 'about.html', context)


def blog_view(request):
    return render(request, 'blog.html')


def cart_view(request):
    return render(request, 'cart.html')






def single_product_view(request):
    return render(request, 'single-product.html')


def contact_view(request):
    return render(request, 'contact.html')

def mailing_email_view(request):
    if request.method == 'POST':
        form = MailingEmailForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MailingEmailForm()

    context = {
        'form': form,
    }
    return render(request, 'mailing_email.html', context)