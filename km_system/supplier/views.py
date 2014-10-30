from datetime import datetime

from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from django.core.urlresolvers import reverse

from models import Supplier

@login_required
def SupplierList(request):
	supplier_list=Supplier.objects.all()
	return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list})

@login_required
def SupplierSearch(request):
	query=request.POST.get('search','')
	print query
	if query:
		qset=(Q(code__icontains=query)|Q(name__icontains=query)|Q(address__icontains=query)|Q(product__icontains=query)|Q(contact__icontains=query)|Q(phone__icontains=query))
		result=Supplier.objects.filter(qset)
		return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list,'query':query})
	else:
		supplier_list=Supplier.objects.all()
		messages=['No result, return all.']
		return render(request,'supplier/supplier_list.html',{'supplier_list':result,'messages':messages})

@login_required
def SupplierAdd(request):
	supplier={}
	messages=[]
	if request.method=='POST':
		c=str((int(Supplier.objects.count())+1)/1000) 
		code=request.POST['code']+' '+c[1:]
		name=request.POST['name']
		address=request.POST['address']
		product=request.POST['product']
		contact=request.POST['contact']
		phone=request.POST['phone']
		fax=request.POST['fax']
		remark=request.POST['remark']
		create_by=request.user
		create_date=datetime.now()
		is_published=True

		new_supplier=Supplier(
			code=code,name=name,address=address,product=product,contact=contact,phone=phone,fax=fax,remark=remark,create_by=create_by,create_date=create_date,is_published=is_published
		)
		new_supplier.save()

		supplier_list=Supplier.objects.all()
		messages.append('Add Success, supplier code: %s' % code)
		return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list,'messages':messages})
		
	supplier['code']=''
	supplier['name']=''
	supplier['address']=''
	supplier['product']=''
	supplier['contact']=''
	supplier['phone']=''
	supplier['fax']=''
	supplier['remark']=''
	supplier['create_by']=request.user
	supplier['create_date']=''
	supplier['is_published']=True
	return render(request,'supplier/supplier_detail.html',{'supplier':supplier})

@login_required
def SupplierDetail(request,pk):
	messages=[]
	if request.method=='POST':
		dt=request.POST['create_date']
		create_date=str(dt)
		username=request.POST['create_by']
		create_by=User.objects.get(username=username)

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
			create_by=create_by,
			create_date=create_date,
			is_published=request.POST.get('is_published',False)
			)
		supplier_desc.save()

		supplier_list=Supplier.objects.filter(is_published=True)
		messages.append('Edit Success!')
		return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list,'messages':messages})

	supplier=get_object_or_404(Supplier,pk=pk)
	create_date=str(supplier.create_date)
	return render(request,'supplier/supplier_detail.html',{'supplier':supplier,'create_date':create_date})

@login_required
def SupplierDelete(request,pk):
	print pk
	messages=[]
	item=Supplier.objects.get(pk=pk)
	item.delete()
	messages.append('Delete Success!')
	supplier_list=Supplier.objects.all()
	return render(request,'supplier/supplier_list.html',{'supplier_list':supplier_list,'messages':messages})


