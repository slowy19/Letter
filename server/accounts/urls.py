from django.urls import path, include
from .views import *

urlpatterns = [
    # path('login/', Login),
    path('signup/', Login.post),
    
    # API
]