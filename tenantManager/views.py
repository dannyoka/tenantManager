from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from . import forms

# Create your views here.

class TenantListView(ListView):
	"""docstring for TenantListView"""
	model = models.Tenant
	template_name = 'tenantManager/templates/tenant_list.html'
	context_name = 'tenant_list'

class TenantCreateView(CreateView):
	"""docstring for TenantCreateView"""
	model = models.Tenant
	fields = ['name','move_in_date','term_end_date','office_number']
	template_name = 'tenantManager/templates/tenant_create_form.html'

class TenantDetailView(DetailView):
	"""docstring for TenantDetailView"""
	model = models.Tenant
	template_name = 'tenantManager/templates/tenant_detail.html'
	context_name = 'tenant_detail'
		
		
		