from django import forms
from . import models

class TenantForm(forms.Form):
	"""docstring for Temamt"""


	class Meta():
		"""docstring for Meta"""
		model = models.Tenant
		fields = ['name','move_in_date','term_end_date','office_number']
		move_in_date = forms.DateField(widget=forms.SelectDateWidget)
		term_end_date = forms.DateField(widget=forms.SelectDateWidget)