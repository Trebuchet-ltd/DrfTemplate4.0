from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from home.forms import SendForm
import yagmail


def send_mail(request):
    form = SendForm()
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data.get('email')
            yag = yagmail.SMTP(settings.EMAIL_HOST_USER, oauth2_file="./credentials.json")
            yag.send(to=[recipient], subject="From Trebuchet 👋", contents="It works, dammit!")
            messages.success(request, 'Success!')
            return redirect('send_mail')
    return render(request, 'sendMail.html', {'form': form})
