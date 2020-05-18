from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:5]
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'home',
               'category': category,
               'sliderdata': sliderdata
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referanslarimiz'}
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
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)




