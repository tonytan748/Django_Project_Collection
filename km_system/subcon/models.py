from django.db import models

from django.contrib.auth.models import User

class Subcon(models.Model):
	code=models.CharField(max_length=10,blank=False,null=False)
	name=models.CharField(max_length=200)
	tel=models.CharField(max_length=15)
	fax=models.CharField(max_length=15)
	contact=models.CharField(max_length=200)
	address=models.CharField(max_length=500)
	scope_of_work=models.CharField(max_length=150)
	remark=models.CharField(max_length=500)
	gst_verification=models.CharField(max_length=10)
	gst_reg_no=models.CharField(max_length=120)
	create_by=models.CharField(max_length=200,default=User)
	create_date=models.DateTimeField(auto_now_add=True)
	edit_by=models.ForeignKey(User)
	edit_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name
	class META:
		orderong=['code']

