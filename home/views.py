import urllib
from bs4 import BeautifulSoup
import requests as req
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from home.forms import SendForm
import yagmail


def parse_html(link):
    web = req.get(link)
    S = BeautifulSoup(web.text, 'lxml')
    return S.prettify()


def send_mail(request):
    form = SendForm()
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            # to3 = 'sky@pip-package.com'
            subject = "From Trebuchet 👋"
            body = "It works, dammit!"
            html = parse_html('https://trebuchet-thankyou.tiiny.site/')
            # img
            recipient = form.cleaned_data.get('email')
            yag = yagmail.SMTP(settings.EMAIL_HOST_USER, oauth2_file="./credentials.json")
            yag.send(to=[recipient], subject=subject, contents=[html])
            messages.success(request, 'Success!')
            return redirect('send_mail')
    return render(request, 'sendMail.html', {'form': form})
