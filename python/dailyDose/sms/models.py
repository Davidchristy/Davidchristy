from django.db import models

# Create your models here.
class User(models.Model):
	pass

class Message(models.Model):
	user_id = models.ForeignKey(User)

	message = models.CharField(max_length=140)