from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from product.models import CommentForm, Comment

# Create your views here.
def index(request):
    return HttpResponse("Cars Page")

@login_required(login_url='/login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST': #form post edildiyse demek
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment() #model ile bağlantı kuruyor
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            # data.rate = form.changed_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderilmiştir, Teşekkür Ederiz")

            return HttpResponseRedirect(url)

        messages.warning(request, "Yorumunuz Kaydedilmedi. Lütfen Kontrol Ediniz!")
        # return HttpResponse("Kaydedilme İşlemi Gerçekleşmedi")
        return HttpResponseRedirect(url)