from django.shortcuts import render

from django.template.context import RequestContext
from spreadsheet.spreadsheet_app.models import Workbooks
import simplejson as json
from django.http import HttpResponse

def index(request):
	template="index.html"

	app_action=request.POST.get('app_action')
	posted_data=request.POST.get('json_data')
	if posted_data is not None and app_action=='save':
		this_sheet=request.POST.get('sheet')
		this_workbook=request.POST.get("workbook_name")
		sheet_id=request.POST.get("sheet_id")

		posted_data=json.dumps(posted_data)
		if(sheet_id):
			wb=Workbooks(id=sheet_id,workbook_name=this_workbook,sheet_name=this_sheet,data=posted_data)
		else:
			wb=Workbooks(workbook_name=this_workbook,sheet_name=this_sheet,data=posted_data)
		wb.save()
	elif app_action=='get_sheets':
		wb_name=request.POST.get('workbook_name')
		sheets=Workbooks.objects.filter(workbook_name=wb_name)
		sheets=[{"sheet_id":i.id,"workbook_name":i.workbook_name.encode("utf-8"),'sheet_name':i.sheet_name.encode('utf-8'),'data':json.loads(i.data.encode("utf-8"))} for i in sheets]
		sheets=json.dumps(sheets)
		return HttpResponse(sheets,mimetype="application/javascript")
	elif app_action=='list':
		workbook=Workbooks.objects.values("workbook_name").distinct()
		workbooks=[i["workbook_name"] for i in workbook]
		return HttpResponse(workbooks,mimetype="application/javascript")

	return render(request,'index.html'.{})
