from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Suite(models.Model):
	"""docstring for Suite"""
	name = models.CharField(max_length=100)
	rent_amount = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return self.name

class Tenant(models.Model):
	"""docstring for Tenant"""
	name = models.CharField(max_length=100)
	move_in_date = models.DateField()
	term_end_date = models.DateField()
	office_number = models.ForeignKey(Suite, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("tenantManager:detail",kwargs={'pk':self.pk})
		
class UserProfileInfo(models.Model):
	"""docstring for UserProfileInfo"""
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	portfolio = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_pics')

	def __str__(self):
		return self.user.username