from django.urls import path

from authentication.views import signin

urlpatterns = [
    path('signin/', signin, name='signin'),
]
