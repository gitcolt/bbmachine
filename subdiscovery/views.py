from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic, View

from .forms import AddDomainForm
from .models import Domain, Subdomain
from utils import send_slack_notification
import requests
import subprocess

import os

class IndexView(generic.ListView):
    template_name = 'subdiscovery/index.html'
    model = Domain
    context_object_name = 'domains'

def find_subdomains(request):
    print(os.getenv('MSG'))
    domains = Domain.objects.all()

    for domain in domains:
        args = ['assetfinder', '--subs-only', domain.name]
        subdomains_found = (subprocess.run(args, check=True, stdout=subprocess.PIPE) \
                        .stdout.decode().split('\n'))
        subdomains_found = filter(None, subdomains_found)

        subdomains_existing = Subdomain.objects.filter(domain=domain).values('name')
        is_first_run = True if len(subdomains_existing) == 0 else False
        not_in_db = set(subdomains_found) - set(sub['name'] for sub in subdomains_existing)

        for e in not_in_db:
            s = Subdomain(domain=domain, name=e)
            s.save()
            if not is_first_run:
                send_slack_notification(f'Found Subdomain: {e}');

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


