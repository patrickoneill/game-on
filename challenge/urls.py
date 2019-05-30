from django.conf.urls import url
from .views import challenges, post_challenge

urlpatterns = [
    url(r'^$', challenges, name='challenges'),
    url(r'^post_challenge/', post_challenge, name='post_challenge'),
]