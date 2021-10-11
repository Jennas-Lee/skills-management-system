from django.urls import path

from authentication.views import signin, signup, signout, mypage

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('mypage/', mypage, name='mypage'),
]
