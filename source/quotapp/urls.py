from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

HOMEPAGE_URL = 'quotes/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('accounts.urls')),
    path('quotes/', include('webapp.urls')),
    path('', RedirectView.as_view(url=HOMEPAGE_URL, permanent=False))
]
