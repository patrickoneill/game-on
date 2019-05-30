from django.conf.urls import url, include
from .views import all_merch

urlpatterns = [
    url(r'^$', all_merch, name='all_merch')    
]