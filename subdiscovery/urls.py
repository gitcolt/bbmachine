from django.urls import path

from . import views

app_name = 'subdiscovery'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('find_subdomains/', views.find_subdomains, name='find_subdomains'),
    path('domain/<int:pk>/', views.DomainView.as_view(), name='domain'),
    #path('subdomain/<int:pk>/', views.SubdomainView.as_view(), name='subdomain'),
    path('add_domain/', views.AddDomainView.as_view(), name='add_domain'),
    path('domain_confirm_delete/<int:pk>/', views.DomainDelete.as_view(), name='domain_delete'),
]
