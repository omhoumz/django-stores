from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Entry


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('hello :')


def list_names(request):

    return render(request, 'list.html', {'entries': Entry.objects.all()})


class AddName(View):
    form_class = Entry
    initial = {'name': '', 'email': ''}
    template_name = 'add.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            name = request.POST.get('name')
            email = request.POST.get('email')
            Entry.objects.create(name=name, email=email)

            return HttpResponseRedirect('/list/')

        return render(request, self.template_name)
