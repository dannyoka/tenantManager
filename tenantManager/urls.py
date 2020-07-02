from django.urls import path,reverse
from . import views

app_name = 'tenantManager'

urlpatterns = [
	path('',views.TenantListView.as_view(),name = 'list'),
	path('create',views.TenantCreateView.as_view(),name='create'),
	path('<pk>',views.TenantDetailView.as_view(),name='detail')


]