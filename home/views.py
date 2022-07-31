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
            def get_input(field_type):
                return form.cleaned_data.get(field_type)
            subject = get_input('subject')
            body = get_input('body')
            html = parse_html(get_input('html'))
            recipient = get_input('email')
            #attachment, img
            yag = yagmail.SMTP(settings.EMAIL_HOST_USER, oauth2_file="~/oauth2_creds.json")
            yag.send(to=[recipient], subject=subject, contents=[body, html])
            messages.success(request, 'Success!')
            return redirect('send_mail')
    return render(request, 'sendMail.html', {'form': form})
