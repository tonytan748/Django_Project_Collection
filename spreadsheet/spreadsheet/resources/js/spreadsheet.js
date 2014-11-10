$(document).ready(function(){
	render_ui();
	openTab();
});



function render_ui(){
	insert_menu_markup();
	insert_grid_markup();
	make_grid_component();
	add_newtab_button();
	insert_open_dialog_markup();
	make_open_dialog();
}

function insert_menu_markup(){
	$("body").prepend('<input type="text" id="workbook_name" name="workbook_name" value="">');
	$("body").prepend('<input id="save" type="button" value="save">');
	$("body").prepend('<input id="open" type="button" value="open">');
	$("body").prepend('<input id="new" type="button" value="new">')
}

function insert_grid_markup(){
	var workbook_widget='<div id="tabs" class="tabs-bottom"><ul><li></li></ul></div>';
	$("body").append(workbook_widget);
}

function make_grid_component(){
	$("#tabs").tabs();
	$(".tabs-bottom .ui-tabs-nav,.tabs-bottom .ui-tabs_nav>*")
	.removeClass("ui-corner-all ui-corner-top")
	.addClass("ui-corner-bottom");
}

function add_newtab_button(){
	$("body").append('<input id="new_tab_button" type="button" value="+">')
}

function insert_open_dialog_markup(){
	var dlg='<div id="dialog_form" title="Open">'+
		'<div id="dialog_form" title="Open">'+
		'<p>Select an archive.</p><form>'+
		'<select id="workbook_list" name="workbook_list">'+
		'</select></form></div>';
	$("body").append(dlg);
}

function make_open_dialog(){
	$("#dialog_form").dialog({
		autoOpen:false,
		modal:true,
		buttons:{
			"OK":function(){
				selected_wb=$('option:selected').attr('value');
				$(this).dialog('close');
				//remove grid,existing forms, and rereate
				$('body').html('');
				render_ui();
				//load grids and create forms with invisible inputs
				load_sheets(selected_wb);
				//place workbook name in text field
				$('#workbook_name').val(selected_wb);
			}
			"Cancel":function(){
				$(this).dialog('close');
			}
		}
	});
}

function openTab(sheet_id){
	numberOfTabs=$("#tabs").tabs("length");
	tab_name="tabs_"+numberOfTabs;

	$("#tabs").tabs("add","#"+tab_name,"Sheet"+numberOfTabs,numberOfTabs);
	$("#"+tab_name).css("display","block");
	$("#tabs").tabs("select",numberOfTabs);

	$("#"+tab_name).css("height","80%");
	$("#"+tab_name).css("height","95%");
	$("#"+tab_name).css("float","left");
	add_grid(tab_name,numberOfTabs);

	//add form for saving this tabs data
	if(!sheet_id){
		$("body").apend(
			'<form method="post" action="?" id="' + tab_name + '_form" name="' + tab_name + '_form">'+
			'<input type="hidden" id="data' + numberOfTabs +'" name="data' + numberOfTabs + '" value="">'+
			'<input type="hidden" id="sheet_id" name="sheet_id" value="">'+
			'</form>');
	}else{
		$("body").append(
			'<form method="post" action="?" id="' + tab_name + '_form" name="' + tab_name  + '_form">'+
			'<input type="hidden" id="data' + numberOfTabs + '" name="data' + numberOfTabs + '" value="">'+
			'<input type="hidden" id="sheet_id" name="sheet_id" value="' + sheet_id + '">'+
			'</form>');
	}
}


var workbock={};
var grid_references={};

function add_grid(grid_name,gridNumber){
	var grid;
	var current_cell=null;
	//column definitions
	var columns=[
		{id:"row",name:"#",field:"num",cssClass:"cell-selection",width:40,cannotTriggerInsert:true,resizeable:false,unselectable:true},
		{id:"a",name:"a",field:"a",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"b",name:"b",field:"b",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"c",name:"c",field:"c",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"d",name:"d",field:"d",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"e",name:"e",field:"e",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"f",name:"f",field:"f",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"g",name:"g",field:"g",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"h",name:"h",field:"h",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"i",name:"i",field:"i",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"j",name:"j",field:"j",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"k",name:"k",field:"k",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"l",name:"l",field:"l",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"m",name:"m",field:"m",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"n",name:"n",field:"n",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"o",name:"o",field:"o",cssClass:"cell-title",width:70,editor:TextCellEditor},
		{id:"p",name:"p",field:"p",cssClass:"cell-title",width:70,editor:TextCellEditor},
	];
	var options={
		editable:true,
		autoEdit:true,
		enableAddRow:true,
		enableCellNavigation:true,
		enableCellRangeSelection:true,
		asyncEditorLoading:true,
		multiSelect:true,
		leaveSpaceForNewRows:true,
		rerenderOnResize:true
	};
	eval("var data"+gridNumber+"=[]");
	workbook["data" + gridNumber]=[];
	for(var i=0;i<100;i++){
		var d=(workbook["data"+gridNumber][i]={});
		d["num"]=i;
		d["value"]="";
	};
	grid=new Slick.Grid($("#"+grid_name),workbook["data"+gridNumber],columns,options);

	grid.onCurrentCellChanged=function(){
		d=grid.getData();
		row=grid.getCurrentCell().row;
		cell=grid.getCurrentCell().cell;
		this_cell_data=d[row][grid.getColumns()[cells].field];
	};

	grid.onBeforeCellEditorDestory=function(){
		d=grid.getData();
		row=grid.getCurrentCell().row;
		cell=grid.getCurrentCell().cell;
		this_cell_data=d[row][grid.getColumns()[cell].field];

		if(this_cell_data && this_cell_data[0] === "="){
			//evaluate Javascript expression, don't use in production!!
			eval("var result=" + this_cell_data.substring(1));
			d[row][grid.getColumns()[cell].field]=result;
		}
	};
	grid_references[grid_name]=grid;
}


$("#new").live("click",function(){
	//delete any existing references
	workbook={};
	grid_references={};
	//remove grid,existing forms, and recreate
	$("body").html("");
	//recreate
	render_ui();
	openTab();
});

#("#save").live("click",function(){
	//Do a foreach on all the grids,the ^= operator gets all the inputs with a name attribute that begins with data
	$("[name^='data']").each(function(index,value){
		var data_index="data"+index;
		var sheet_id=$("#tabs_" + index + "_form").find("#sheet_id").val();
		if(sheet_id!==''){
			sheet_id=eval(sheet_id);
		}
		//convenience variable for readability
		var data2post=$.JSON.encode(workbook[data_index]);
		$("#" + data_index).val(data2post);
		$.post('{% url index %}',
			{'app_action':'save','sheet_id':sheet_id,'workbook_name':$('#workbook_name').val(),'sheet':data_index,'json_data':data2post});
	});
});


function load_sheets(workbook_name){
	#("#workbook_list").load('{% url index%}',
		{'app_action':'get_sheets','workbook_name':workbook_name},
		function(sheets,resp,t){
			sheets=$.JSON.decode(sheets);
			workbook={};//reset
			grid_reference={};
			$.each(sheets,function(index,value){
				//add to workbook object
				var sheet_id=value["sheet_id"];
				openTab(sheet_id);
				//By calling eval,we translate value from a string to a javascript object
				workbook[index]=eval(value["data"]);
				//insert data into hidden
				$("#data"+index).attr("value",workbook[index]);
				grid_references["tab_"+index].setData(workbook[index]);
				grid_references["tab_"+index].render();
			});
		});
}

$("#open").live('click',function(){
	//load is used for doing asynchronous loading of data
	$("#workbook_list").load("{% url index %}",{"app_action":"list"},
	function(workbooks,success){
		workbooks=$.JSON.decode(workbooks);
		$.each(workbooks,function(){
			$("#workbook_list").append(
				'<option value="' + value + '" >' + value + '</option>');
		});
	});
	$("#dialog_form").dialog("open");
});
