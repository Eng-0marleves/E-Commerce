from django.db import models
from django.utils.html import escape
from django.utils.html import format_html


class User(models.Model):
	first_name = models.CharField(max_length=75)
	last_name = models.CharField(max_length=75)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	img =	models.ImageField(upload_to='user_images/', null=True, blank=True)

	