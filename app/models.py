from django.db import models

# Create your models here.

class todo(models.Model):
	affair = models.CharField(max_length = 200, null = False)
	complete = models.BooleanField(default = False)
	date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.affair
