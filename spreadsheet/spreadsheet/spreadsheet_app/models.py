from django.db import models

class Workbooks(models.Model):
	workbook_name=models.CharField(max_length=30)
	sheet_name=models.CharField(max_length=30)
	data=models.TextField()
