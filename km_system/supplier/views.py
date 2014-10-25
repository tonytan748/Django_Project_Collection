from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from models import Supplier

@login_required
def SupplierList(request):
	supplier_list=Supplier.objects.filter(is_published=True)
	return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list})
	
@login_required
def SupplierDetail(request,pk):
	supplier=Supplier.objects.get(pk=pk)
	return render(request,reverse('supplier_detail',kwargs={'supplier':supplier})
	
@login_required
def SupplierDelete(request,pk):
	messages=[]
	if request.mothed=='POST':
		if pk:
			item=Supplier.objects.get(pk=pk)
			item.delete()
			messages.append('Delete Success!')
			return HttpResponseRedirect(reverse('list/'),{'messages':messages})
		else:
			messages.append('please check your delete item.')
			return HttpResoponseRedirect('list/',{'messages':messages})
	return HttpResponseRedirect('list/')


#def SupplierListView(ListView):
#	model=Supplier
#	def get_context_data(self,**kwargs):
#		context=super(SupplierList,self).get_context_data(**kwargs)
#		context['published']=Supplier.objects.filter(is_published=True)
#		return context

#@login_required
#def SupplierDetailView(DetailView):
#	model=Supplier
'''
@login_required
def SupplierDelete(request,pk):
	if request.method=='POST':
		if pk:
			item=Supplier.objects.get(pk=pk)
			item.delete()
			messages.append('delete success!')
			return HttpResponseRedirect(reverse('supplier:list'),{'messages':messages})
		else:
			messages.append('Please check your delete item.')
			return HttpResponseRedirect('supplier:list',"messages":messages)
	return HttpResponseRedirect('supplier:list')
'''
