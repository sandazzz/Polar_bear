from django.urls import path
from polar_bear.views import *

urlpatterns = [
    path('', list_article, name='list_article'),
    path('article/<int:id>', article, name='article'),
    ]