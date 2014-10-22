from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Post

class PublishedPostsMixin(object):
	def get_queryset(self):
		return self.model.objects.filter(published=True)

class PostListView(PublishedPostMixin,ListView):
	model=Post

class PostDetailView(PublishedPostMixin,DetailView):
	model=Post

'''
def blog_list(request,*args,**kwargs):
	post_list=Post.objects.filter(published=True)
	template_name="post_list.html"
	context={'post_list':post_list}
	return render(request,template_name,context)

def blog_detail(request,,pk,*args,**kwargs):
	post=Post.objects.get(pk=pk,published=True)
	template_name='blog/post_detail.html'
	context={'post':post}
	return render(request,template,context)
'''
