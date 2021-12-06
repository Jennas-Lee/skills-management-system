from django.urls import path

from notice.views import list_notice, create_notice, viewer_notice

urlpatterns = [
    path('', list_notice, name='list_notice'),
    path('create/', create_notice, name='create_notice'),
    path('viewer/<int:id>/', viewer_notice, name='viewer_notice'),
]
