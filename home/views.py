from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:5]
    category = Category.objects.all()
    lastcars = Product.objects.all().order_by('category_id')[:6]
    randomcars = Product.objects.all().order_by('?')[:4]
    lastcarsnews = Product.objects.all()[:4]


    context = {'setting': setting,
               'page': 'home',
               'category': category,
               'sliderdata': sliderdata,
               'lastcars': lastcars,
               'lastcarsnews': lastcarsnews,
               'randomcars': randomcars
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               'page': 'referanslarimiz'}
    return render(request, 'referanslarimiz.html', context)



def iletisim(request):
    #formu kaydetmek için bu fonksiyon yazıldı
    if request.method == 'POST': #form post ediliyor
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir, Teşekkür Ederiz")
            return HttpResponseRedirect ('/iletisim')

    #forma ulaşmak için bu kodlar yazıldı
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,
               'category': category,
               'form': form
               }
    return render(request, 'iletisim.html', context)

def category_products(request,id,slug):

    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    cars = Product.objects.filter(category_id=id, status='True')
    context = {'cars': cars,
               'category': category,
               'categorydata': categorydata
               }
    return render(request, 'araclar.html', context)

def cars_details(request, id, slug):
    category = Category.objects.all()
    cars = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'cars': cars,
               'category': category,
               'images': images,
               'comments': comments
               }

    return render(request, 'arac_detail.html', context)


def cars_search(request):
    #formu kaydetmek için bu fonksiyon yazıldı
    if request.method == 'POST': #form post ediliyor
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query'] # formdan  bilgiyi alır
            cars = Product.objects.filter(title__icontains=query)

            context = {'cars': cars,
                       'category': category
                       }
            return render(request, 'cars_search.html', context)

    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Hoşgeldiniz")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatası ! Kullanıcı adı ya da şifre yanlış")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Kayıt Hatası !"+str(form.error_messages))
            return HttpResponseRedirect('/signup')
    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup.html', context)
