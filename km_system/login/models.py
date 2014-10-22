from django.db import models

from django.contrib.auth.models import User


class ManagementItem(models.Model):
	user=models.ForeignKey(User)
	ITEMS=(('SUPPLIER','supplier'),('MATERIAL','material'),('PROJECT','project'),('PO','po'),('GR','gr'),('ISSUE','issue'))
	management_item=models.CharField(max_length=20,choices=ITEMS,default='PO')
	create_date=models.DateTimeField(auto_now_add=True)
	create_date=models.CharField(max_length=100)

	def __unicode__(self):
		return self.management_item

	class META:
		ordering=['user']
