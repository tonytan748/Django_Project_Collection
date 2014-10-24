from django.db import models

from django.contrib.auth.models import User

class Supplier(models.Model):
	code=models.CharField(max_length=10,blank=False,null=False)
	name=models.CharField(max_length=200,blank=False,null=False)
	address=models.TextField()
	product=models.CharField(max_length=100)
	contact=models.CharField(max_length=120)
	phone=models.CharField(max_length=50)
	fax=models.CharField(max_length=50)
	remark=models.TextField()
	create_by=models.ForeignKey(User)
	create_date=models.DateTimeField(auto_now_add=True)
	is_published=models.BooleanField(default=True)

	class META:
		ordering=['supplier_name']

	def __unicode__(self):
		return self.name
