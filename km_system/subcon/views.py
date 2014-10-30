from datetime import datetime

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin


from models import Subcon
#from forms import SubconForm

class SubconListView(LoginRequiredMixin,ListView):
	model=Subcon
	paginate_by=25
	
class SubconUpdateView(LoginRequiredMixin,UpdateView):
	model=Subcon
#	template_name_suffix='subcon/subcon_detail.html'
	template_name='subcon/subcon_detail.html'

	def get_success_url(self):
		return reverse('list')

class SubconAddView(LoginRequiredMixin,CreateView):
	form_class=SubconForm
	model=Subcon
	
	def form_valid(self,form):
		form.instance.create_by=self.request.user
		return super(SubconAddView,self).form_valid(form)

