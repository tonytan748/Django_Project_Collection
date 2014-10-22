from django.db import models

class Book(models.Model):
	isbn=models.CharField('ISBN',max_length=13,unique=True)
	title=models.CharField('book name',max_length=200)
	subtitle=models.CharField('subtitle',max_length=200,blank=True)
	pages=models.IntegerField('pages',blank=True)
	author=models.CharField('author',max_length=60)
	translator=models.CharField('translator',max_length=60)
	price=models.CharField('price',max_length=60,blank=True)
	publisher=models.CharField('publisher',max_length=200,blank=True)
	pubdate=models.CharField('pub date',max_length=60,blank=True)
	cover_img=models.URLField('cover image',blank=True)
	summary=models.TextField('content',blank=True,max_length=2000)
	author_intro=models.TextField('author information',blank=True,max_length=2000)

	class Meta:
		verbose_name='BOOKS'
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return str(self.title)
	
