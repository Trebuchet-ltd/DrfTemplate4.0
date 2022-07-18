from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Setup the URLs and include login URLs for the browsable API.
from .views import send_mail

router = DefaultRouter()

urlpatterns = [
    path(r'', include(router.urls)),
    path('sendmail/', send_mail, name='send_mail')
]