from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic, View

from .forms import AddDomainForm
from .models import Domain, Subdomain
from utils import send_slack_notification
import requests
import subprocess
from . import find_subdomains

import os

class IndexView(generic.ListView):
    template_name = 'subdiscovery/index.html'
    model = Domain
    context_object_name = 'domains'

def find_subdomains_view(request):
    find_subdomains();
    return redirect('subdiscovery:index')

class DomainView(View):
    def get(self, request, pk):
        domain = get_object_or_404(Domain, pk=pk)
        subdomains = Subdomain.objects.filter(domain=domain)
        return render(request, 'subdiscovery/domain.html', {'domain': domain, 'subdomains': subdomains})

class AddDomainView(generic.edit.CreateView):
    template_name = 'subdiscovery/add_domain.html'
    model = Domain
    fields = ['name']
    success_url = reverse_lazy('subdiscovery:index')

class DomainDelete(generic.edit.DeleteView):
    template_name = 'subdiscovery/domain_confirm_delete.html'
    model = Domain
    success_url = reverse_lazy('subdiscovery:index')


