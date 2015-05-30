from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class Index(View):

    def get(self, request):
        context = {}
        return render(request, 'trafficking/index.html', context)

    def post(self, request):
        pass

