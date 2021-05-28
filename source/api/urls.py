from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import QuoteListView, QuoteCreateView, QuoteDetailView
from api import views


app_name = 'api'

article_urls = [
    path('', QuoteListView.as_view(), name='quotes'),
    path('create', QuoteCreateView.as_view(), name='create'),
    path('<int:pk>/', QuoteDetailView.as_view(), name='view'),

]


urlpatterns = [
    path('quotes/', include(article_urls)),
]