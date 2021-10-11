from django.urls import path

from notice.views import list_notice, create_notice

urlpatterns = [
    path('', list_notice, name='list_notice'),
    path('create/', create_notice, name='create_notice')
]
