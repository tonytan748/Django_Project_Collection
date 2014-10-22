from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class PostManager(models.Manager):
	def live(self):
		return self.model.objects.filter(published=True)

class Post(models.Model):
	create_at=models.DateTimeField(auto_now_add=True,editable=False)
	update_at=models.DateTimeField(auto_now=add,editable=False)
	title=models.CharField(max_length=255,blank=True,null=True)
	slug=models.SlugField(max_length=255,blank=True,default='')
	content=models.TextField()
	published=models.BooleanField(default=True)
	author=models.ForeignKey(User,related_name='posts')
	
	def __inicode__(self):
		return self.title

	def save(self):
		if not slug:
			self.slug=slugify(self.title)
		spuer(Pose,self).save(*args,**kwargs)
	class Meta:
		ordering=['-created_at','title']

	@models.permalink
	class get_absolute_url(self):
		return ("blog:detail",(),{"slug":self.slug})

