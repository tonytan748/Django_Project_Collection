from django.shortcuts import render,get_object_or_404,render_to_response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

#from forms import SupplierForm
from models import Supplier

@login_required
def SupplierList(request):
	supplier_list=Supplier.objects.filter(is_published=True)
	return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list})

@login_required
def SupplierDetail(request,pk):
	messages=[]
	if request.method=='POST':
		supplier_desc=Supplier(
			pk=pk,
			code=request.POST['code'],
			name=request.POST['name'],
			address=request.POST['address'],
			product=request.POST['product'],
			contact=request.POST['contact'],
			phone=request.POST['phone'],
			fax=request.POST['fax'],
			remark=request.POST['remark'],
#			create_by=request.POST['create_by'],
			create_date=request.POST['create_date'],
			is_published=request.POST['is_published']
			)
		supplier_desc.save()
		

		supplier_list=Supplier.objects.filter(is_published=True)
		messages.append('Edit Success!')
		return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list,'messages':messages})

	supplier=get_object_or_404(Supplier,pk=pk)
	return render(request,'supplier/supplier_detail.html',{'supplier':supplier})

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

