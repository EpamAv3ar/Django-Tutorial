from django.urls import path
from ecom_store.views import (
    home,
)

urlpatterns = [
    path('', home, name='home'),
]
