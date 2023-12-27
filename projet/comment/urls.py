from django.urls import path
from comment.views import *

urlpatterns = [
    path('comment/', comment, name='comment'),
    path('', clear_comments, name='clear_comments'),
]