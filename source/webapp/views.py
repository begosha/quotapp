import random

from django.db.migrations import serializer
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from rest_framework import status
from rest_framework.response import Response

from .models import Quote


class IndexView(View):

    def get(self, request, *args, **kwargs):
        sessionid = request.session.get('session', {})
        sessionid['id'] = self.request.COOKIES['sessionid']
        request.session['session']=sessionid
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        quote = Quote()
        quote.text = self.request.POST.get('quote')
        quote.author = self.request.POST.get('author')
        quote.email = self.request.POST.get('email')
        quote.save()
        return render(request, 'index.html')

    def put(self, request, *args, **kwargs):
        if request.session['session']['id'] == self.request.COOKIES['sessionid']:
            return HttpResponseForbidden()
        else:
            pk = int((self.request.body).decode('utf-8'))
            quote = Quote.objects.get(id=pk)
            quote.rating += 1
            quote.save()
            return render(request, 'index.html')

    def delete(self, request, *args, **kwargs):
        if request.session['session']['id'] == self.request.COOKIES['sessionid']:
            return HttpResponseForbidden()
        else:
            pk = int((self.request.body).decode('utf-8'))
            quote = Quote.objects.get(id=pk)
            quote.rating -= 1
            quote.save()
            return render(request, 'index.html')

