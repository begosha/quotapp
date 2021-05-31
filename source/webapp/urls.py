from django.urls import path
from .views import IndexView


app_name = 'quotes'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
]
