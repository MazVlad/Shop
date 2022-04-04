from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import *
from .models import *
from django.views.generic import ListView,DetailView,CreateView
from cart.forms import CartAddProductForm

class Index(ListView):
    paginate_by = 5
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        cart_product_form = CartAddProductForm()
        context['cats'] = cats
        context['cart_product_form']=cart_product_form
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

'''def index(request):
    cats = Category.objects.all()
    products = Product.objects.filter(is_published=True)
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/index.html', {
        'page_obj': page_obj,
        'cats' : cats,
        'products' : products,
        'cart_product_form' : cart_product_form

    })'''

def show_category(request, cat_id):
    posts = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'posts': posts,'cats':cats,'cart_product_form':cart_product_form}
    return render(request, 'main/category.html', context=context)

class ShowPost(DetailView):
    model = Product
    template_name = 'main/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        context['cats'] = cats
        return context




class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        cats = Category.objects.all()
        context['cats'] = cats
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:index')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        context['title'] = "Авторизация"
        return context

    def get_success_url(self):
        return reverse_lazy('main:index')

def logout_user(request):
    logout(request)
    return redirect('main:login')

class search(ListView):
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Product.objects.filter(name__iregex=self.request.GET.get("search"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        return context