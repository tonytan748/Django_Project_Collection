from django.db import models

from django.contrib.auth.models import User

class ManagementList(models.Model):
	itemname=models.CharField(max_length=200,unique=True)
	
	def __unicode__(self):
		return self.itemname

class ManagementItem(models.Model):
	user=models.ForeignKey(User)
	management_item=models.ForeignKey(ManagementList,to_field='itemname')
	create_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.management_item

	class META:
		ordering=['user']
