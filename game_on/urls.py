"""game_on URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from merchandise import urls as urls_merch
from basket import urls as urls_basket
from checkout import urls as urls_checkout
from search import urls as urls_search
from merchandise.views import all_merch
from challenge import urls as urls_challenges
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_merch, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^merchandise/', include(urls_merch)),
    url(r'^basket/', include(urls_basket)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^challenge/', include(urls_challenges)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
