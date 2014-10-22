from django.db import models

from django.contrib.auth.models import User

ITEMS=('','','','','','')

class ManagementItem(modelsi.Model):
	user=models.ForeignKey(User)
	management_item=models.CharField(max_length=20,choices=ITEMS)
	create_date=models.DateTimeField(auto_add_now=True)
	create_date=models.CharField(max_length=100)

	def __unicode__(self):
		return self.management_item

	class META:
		ordering=['user']
