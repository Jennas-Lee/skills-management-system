from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView

from index.urls import urlpatterns as index_urls
from authentication.urls import urlpatterns as auth_urls
from notice.urls import urlpatterns as notice_urls

urlpatterns = [
    path('', include(index_urls)),
    path('auth/', include(auth_urls)),
    path('notice/', include(notice_urls)),

    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path('admin/', admin.site.urls),
]
