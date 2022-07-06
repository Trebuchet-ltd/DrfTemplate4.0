from django.urls import path, include

from .views import signin, log_out, signup


urlpatterns = [
    path('login/', signin),
    path('logout/', log_out),
    path('signup/', signup),
    path('accounts/', include('allauth.urls'))
]
