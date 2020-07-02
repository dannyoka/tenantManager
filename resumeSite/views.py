from django.views.generic import TemplateView

class HomePageView(TemplateView):
	"""docstring for HomePageView"""
	template_name = 'index.html'

class AboutView(TemplateView):
	"""docstring for AboutView"""
	template_name = 'about.html'

class PricingView(TemplateView):
	"""docstring for PricingView"""
	template_name = 'pricing.html'

class RequestMoreInfoView(TemplateView):
	"""docstring for RequestMoreInfoView"""
	template_name = 'request_more_info.html'
