# flake8: noqa

GET_POS_STATUS = r"""
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!-- Copyright &copy; 2017-2022 Hewlett Packard Enterprise Development LP. -->
<html>

<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>PoE Port Configuration</title>
<link rel="shortcut icon" href="/htdocs/login/favicon.ico?">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/jquery-ui-1.12.1.custom.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/jquery/datatables_1_9_4/css/jquery.dataTables_themeroller.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_datatables_custom.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_common_pages.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/tabs.css">
<!--[if ie 7]>
<link rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_browser_fixups_ie7.css" type="text/css">
<![endif]-->
<!--[if gte ie 7]>
<link rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_browser_fixups_ie7plus.css" type="text/css">
<![endif]-->
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/jquery_3_5_1/jquery-3.5.1.min.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/jquery_ui_1_12_1/jquery-ui-1.12.1.min.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/datatables_1_9_4/jquery.dataTables.min.js"></script>
</head>

<body class="ui-state-default fp_jqtds_page_body fp_corner_bottom">
<a name="focus_top" id="focus_top"></a>

<div id="fp_div_page_title_bar" class="fp_jqtds_h1">
<div id="fp_div_page_title_text">PoE Port Configuration</div>&nbsp;
<div id="fp_div_title_bar_tooltip">
<a class="fp_anchor_tooltip" href="/htdocs/lang/en_us/help/base/help_poe_port_cfg.lsp" target="_blank">
<img src="/htdocs/static/bt1671095783/images/icon_help_black24-helpText.png" title="Help" alt="Help" border="0">
</a>
</div><!-- fp_div_title_bar_tooltip -->
</div><!-- fp_div_page_title_bar -->

<div class="fp_page_container">

<form id="form1" name="form1" method="post" action="/htdocs/pages/base/poe_port_cfg.lsp">

<div class="fp_sub_container">
<div id="dynamic_dt1"></div>
</div> <!-- fp_sub_container -->

<div id="page_buttons" class="fp_button_row">
<input class="fp_button ui-button ui-widget ui-state-default" type="submit" id="b_form1_refresh" name="b_form1_refresh" value="Refresh" onclick="jslib_b_pressed_g='refresh';">
&nbsp;
<input class="fp_button ui-button ui-widget ui-state-default fp_dt_button" type="button" id="b_form1_dt_remove" name="b_form1_dt_remove" value="Edit" >
&nbsp;
<input class="fp_button ui-button ui-widget ui-state-default fp_dt_button" type="button" id="b_form1_dt_add" name="b_form1_dt_add" value="Edit All" >
&nbsp;
<input class="fp_button ui-button ui-widget ui-state-default fp_dt_button" type="submit" id="b_form1_dt_multi_edit" name="b_form1_dt_multi_edit" value="Reset" onclick="jslib_b_pressed_g='dt_multi_edit';">
&nbsp;
<input class="fp_button ui-button ui-widget ui-state-default fp_dt_button" type="button" id="b_form1_dt_details" name="b_form1_dt_details" value="Details" >
</div> <!-- fp_button_row -->

</form> <!-- form1 -->

</div><!-- fp_page_container -->

<script type="text/javascript" language="JavaScript">
<!--
  var jslib_msgs = parent.jslib_msgs_tbl;
-->
</script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/js/web-utils-combo.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/plugins/jquery-plugins-combo.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/datatables_1_9_4/jquery.dataTables-plugins.js"></script>
<script type="text/javascript" src="/htdocs/lang/en_us/culture/globalize.culture.en-US.20120606.js"></script>

<script type="text/javascript" language="JavaScript">
<!--

var aDataSet = [
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_1" value="1"><label></label>', '1', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_2" value="2"><label></label>', '2', 'Disabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
];

  var aColumns = [
    { "sTitle": '<input type="checkbox" class="chkall" name="chkall" id="chkall" value="chkall"><label></label>',       "bSearchable": false, "bSortable": false, "sWidth": "2%" },
    { "sTitle": "Interface",         "sType": "intf-sort", "sWidth": "5%" },
    { "sTitle": "Admin Mode",        "sType": "html" },
    { "sTitle": "Priority",          "sType": "html" },
    { "sTitle": "Schedule",          "sType": "html" },
    { "sTitle": "High Power Mode",   "sType": "html" },
    { "sTitle": "Power Detect Type", "sType": "html" },
    { "sTitle": "Power Limit Type",  "sType": "html" },
    { "sTitle": "Status",            "sType": "html" },
    { "sTitle": "Fault Status",      "sType": "html" }
  ];

// Edit button query string callback function
// This function name is specified as the 'fn' parameter on 'modal_button_attrib' for the 'edit' button
function fnEdit()
{
  var qString = '';
  var intfStr = [];

  $(".chkrow:checked").each(function(idx) {
    intfStr[idx] = $(this).val();
  });

  qString = '?intfStr='+intfStr;
  return qString;
}

// Edit All button query string callback function
// This function name is specified as the 'fn' parameter on 'modal_button_attrib' for the 'editAll' button
function fnEditAll()
{
  return '?intfStr=all';
}

// Details button query string callback function
function fnDetail(argStr)
{
  var selected = fp_dt_get_selected($("#sorttable1"));
  var qString = '';

  if (selected.length == 1)
  {
    // Specify internal interface number
    var values = selected[0].cells[0].firstChild.value.split(" ");
    if(values.length > 0)
    {
      qString = '?intfStr=' + values[0];
    }
  }
  return qString;
}

$(document).ready( function ()
{

  for (var i = 0; i < aDataSet.length; i++)
  {
    var limit = aDataSet[i].pop();
    if (limit != "nil")
    {
      limit = (limit / 1000);
      aDataSet[i][7] = aDataSet[i][7] + " (" + limit + " W)";
    }
  }

  // Define datatable
  $('#dynamic_dt1').html( '<table cellpadding="0" cellspacing="0" border="0" class="display" id="sorttable1"><\/table>' );
  fp_dt_create("#sorttable1", { aaData: aDataSet, aoColumns: aColumns, dt_btn: true, multi_select:true, rw: true });


});

-->
</script>

<script type="text/javascript" language="JavaScript">
<!--
$(document).ready( function()
{
  var page_is_valid = true;

  // format all culture-specific elements using the current locale
  culture_format(parent.culture);


    var myNav = navigator.userAgent.toLowerCase();
    var isIe = false;
    if (myNav.indexOf('msie') != -1)
    {
      var myVer = parseInt(myNav.split('msie')[1]);
    }

    if ((isIe == true) && (myVer < 8)) {
    $('input[type=radio],[type=checkbox]').live('click', function () {
      this.blur();
      this.focus();
    });
  }

  $(':input').bind('keypress', function(e) {
    var key = (window.event) ? window.event.keyCode : e.which;  // IE vs. FF
    var $this = $(this);
    if ( ($this.is(':not(:button, :submit, :reset, textarea)')) ) {
      return (key != 13);
    }
  });

  $(".fp_button").button();
    $(".fp_button_cancel").button();

  $('form input[type="reset"]').click(function(e) {
   if( $('#sorttable1').length ){
    fp_dt_reset_handler("#sorttable1");
   }
    return jslib_form_reset(this.form);
  });

  $(":submit,:button").click(function(e) {
    // remember which button was clicked last by storing into hidden field
    var button = $(this).attr("id");
    var form_id = $(e.target).closest("form").attr("id");
    if (form_id)
    {
      $("#b_"+form_id+"_clicked").val(button);
    }
    page_is_valid = jslib_form_validate(document.forms[0]);

    return page_is_valid;
  });

  // add a hidden field to each form to record which submit button
  // was clicked so that it gets presented in the POST data
  $("form").each(function() {
    var $this = $(this);
    var bid = "b_" + $this.attr("id") + "_clicked";
    var b_clicked = '<input type="hidden" id="' + bid + '" name="' + bid + '">';
    $(b_clicked).appendTo($this);
  });
  // Bind to the click event for all the matching 'b_form1_dt_remove' buttons to open a page as a modal dialog
  $('[id*="b_form1_dt_remove"]').click( function() {
    var qStr = fnEdit();
    main_modal_page_open('/htdocs/pages/base/poe_port_cfg_modal.lsp' + qStr, 'Edit PoE Port Configuration', '680', '370', {  btnPost : "Apply", btnClose : "Cancel" } );
  });

  // Bind to the click event for all the matching 'b_form1_dt_add' buttons to open a page as a modal dialog
  $('[id*="b_form1_dt_add"]').click( function() {
    var qStr = fnEditAll();
    main_modal_page_open('/htdocs/pages/base/poe_port_cfg_modal.lsp' + qStr, 'Edit PoE Port Configuration', '680', '370', {  btnPost : "Apply", btnClose : "Cancel" } );
  });

  // Bind to the submit event for 'b_form1_dt_multi_edit' to open a modal confirm dialog
  $('#form1').submit( function(e) {
    var pattern = /dt_multi_edit/gi;
    if (jslib_b_pressed_g.match(pattern)) {
      e.preventDefault();
      main_confirm_dialog_open('dt_multi_edit', 'Are you sure you want to reset the selected row(s)?');    }
  });

  // Bind to the click event for all the matching 'b_form1_dt_details' buttons to open a page as a modal dialog
  $('[id*="b_form1_dt_details"]').click( function() {
    var qStr = fnDetail();
    main_modal_page_open('/htdocs/pages/base/poe_port_cfg_details.lsp' + qStr, 'PoE Port Details', '680', '350', {  btnClose : "Close" } );
  });

  $(window).resize(function() {
    if(this.resizeTO) clearTimeout(this.resizeTO);
    this.resizeTO = setTimeout(function() {
      $(this).trigger('resizeEnd');
      }, 500);
  });
  $(window).bind('resizeEnd', function() {
      iframe_auto_resize();
  });
  iframe_auto_resize();
  $('form input[type="submit"]').click(function(e) {
    var form_id = $(e.target).closest("form").attr("id");
    var f_s = "b_"+form_id+"_submit";
    var f_r = "b_"+form_id+"_refresh";
    var f_click = $("#b_"+form_id+"_clicked").val();
    if (((f_click == f_s) || (f_click == f_r)) && page_is_valid)
    {
      parent.progress_modal_open();
    }
  });
  parent.progress_modal_handler(parent.ple.PAGE_LOADED);

  focus_init("focus_top");
});
-->
</script>

</body>
</html>
"""

GET_SERIAL_NUMBER = r""""
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!-- Copyright &copy; 2017-2022 Hewlett Packard Enterprise Development LP. -->
<html>

<head>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Dashboard</title>
<link rel="shortcut icon" href="/htdocs/login/favicon.ico?">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/jquery-ui-1.12.1.custom.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/jquery/datatables_1_9_4/css/jquery.dataTables_themeroller.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_datatables_custom.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_common_pages.css">
<link type="text/css" media="screen" rel="stylesheet" href="/htdocs/static/bt1671095783/css/tabs.css">
<!--[if ie 7]>
<link rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_browser_fixups_ie7.css" type="text/css">
<![endif]-->
<!--[if gte ie 7]>
<link rel="stylesheet" href="/htdocs/static/bt1671095783/css/style_browser_fixups_ie7plus.css" type="text/css">
<![endif]-->
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/jquery_3_5_1/jquery-3.5.1.min.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/jquery_ui_1_12_1/jquery-ui-1.12.1.min.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/datatables_1_9_4/jquery.dataTables.min.js"></script>
</head>

<body class="ui-state-default fp_jqtds_page_body fp_corner_bottom">
<a name="focus_top" id="focus_top"></a>

<div id="fp_div_page_title_bar" class="fp_jqtds_h1">
<div id="fp_div_page_title_text">Dashboard</div>&nbsp;
<div id="fp_div_title_bar_tooltip">
<a class="fp_anchor_tooltip" href="/htdocs/lang/en_us/help/base/help_dashboard.lsp" target="_blank">
<img src="/htdocs/static/bt1671095783/images/icon_help_black24-helpText.png" title="Help" alt="Help" border="0">
</a>
</div><!-- fp_div_title_bar_tooltip -->
</div><!-- fp_div_page_title_bar -->

<div class="fp_page_container">

<form id="form1" name="form1" method="post" action="/htdocs/pages/base/dashboard.lsp">

<div class="fp_sub_container">
<table class="fp_page_table_class" id="table_1" cellpadding="0" cellspacing="0" >
<tbody>

<!-- System Information -->
<tr>
<td colspan="3"><div class="fp_jqtds_h2 fp_sub_title fp_sub_title_first">System Information</div></td>
</tr>


<tr>  <!-- System Description -->
<td class="ui-widget-content fp_data_label_25w">System Description</td>
<td class="ui-widget-content fp_data_value" id="sys_descr">HPE OfficeConnect Switch 1820 24G PoE+ (185W) J9983A,  PT.02.17,  Linux 3.6.5,  U-Boot 2012.10-00119 (Aug 31 2018 - 10:12:27)</td>
</tr>

<tr>  <!-- System Name -->
<td class="ui-widget-content fp_data_label_25w">System Name</td>
<td class="ui-widget-content fp_data_value">
<input class="fp_inputfield" type="text" id="sys_name" name="sys_name" size="20" maxlength="64"
value="switch">&nbsp;&nbsp;(0 to 64 characters)</td>
</tr>

<tr>  <!-- System Location -->
<td class="ui-widget-content fp_data_label_25w">System Location</td>
<td class="ui-widget-content fp_data_value"><input class="fp_inputfield" type="text" id="sys_location" name="sys_location" size="20" maxlength="255"
value="">&nbsp;&nbsp;(0 to 255 characters)</td>
</tr>

<tr>  <!-- System Contact -->
<td class="ui-widget-content fp_data_label_25w">System Contact</td>
<td class="ui-widget-content fp_data_value">
<input class="fp_inputfield" type="text" id="sys_contact" name="sys_contact" size="20" maxlength="255"
value="">&nbsp;&nbsp;(0 to 255 characters)</td>
</tr>

<tr>  <!-- System Object ID -->
<td class="ui-widget-content fp_data_label_25w">System Object ID</td>
<td class="ui-widget-content fp_data_value" id="sys_obj_id">1.3.6.1.4.1.11.2.3.7.11.171</td>
</tr>

<tr>  <!-- System Up Time -->
<td class="ui-widget-content fp_data_label_25w">System Up Time</td>
<td class="ui-widget-content fp_data_value" id="sys_up_time">238 days, 6 hours, 34 mins, 38 secs</td>
</tr>

<tr>  <!-- Current Time -->
<td class="ui-widget-content fp_data_label_25w">Current Time</td>
<td class="ui-widget-content fp_data_value" id="curr_time">
15:20:22</td>
</tr>

<tr>  <!-- Date -->
<td class="ui-widget-content fp_data_label_25w">Date</td>
<td class="ui-widget-content fp_data_value" id="curr_date">
November 11, 2024</td>
</tr>

</tbody>
</table>
</div> <!-- fp_sub_container -->

<div class="fp_sub_container">
<table class="fp_page_table_class" id="table_2" cellpadding="0" cellspacing="0" >
<tbody>

<!-- Device Information -->
<tr>
<td colspan="3"><div class="fp_jqtds_h2 fp_sub_title">Device Information</div></td>
</tr>

<tr>  <!-- Software Version -->
<td class="ui-widget-content fp_data_label_25w">Software Version</td>
<td class="ui-widget-content fp_data_value" id="sw_version" colspan="2">PT.02.17</td>
</tr>

<tr>  <!-- Operating System -->
<td class="ui-widget-content fp_data_label_25w">Operating System</td>
<td class="ui-widget-content fp_data_value" id="operating_sys" colspan="2">Linux 3.6.5</td>
</tr>

<tr>  <!-- Serial Number -->
<td class="ui-widget-content fp_data_label_25w">Serial Number</td>
<td class="ui-widget-content fp_data_value" id="serial_number" colspan="2">TEST_SERIAL_NUMBER</td>
</tr>

</tbody>
</table>
</div> <!-- fp_sub_container -->

<div class="fp_sub_container">
<table class="fp_page_table_class" id="table_3" cellpadding="0" cellspacing="0" >
<tbody>

<!-- System Resource Usage -->
<tr>
<td colspan="3"><div class="fp_jqtds_h2 fp_sub_title">System Resource Usage</div></td>
</tr>

<tr>  <!-- CPU Utilization (60 Second Average) -->
<td class="ui-widget-content fp_data_label">CPU Utilization (60 Second Average)</td>
<td class="ui-widget-content fp_data_value"  id="cpu_util">
<div class="fp_progressbar" id="cpu_util_prog_bar"></div>
<div class="ui-widget-content fp_progressbar_val" id="cpu_util_prog_bar_val">32 %</div>
</td>
</tr>

<tr>  <!-- Memory Usage -->
<td class="ui-widget-content fp_data_label">Memory Usage</td>
<td class="ui-widget-content fp_data_value"  id="mem_util">
<div class="fp_progressbar" id="mem_util_prog_bar"></div>
<div class="ui-widget-content fp_progressbar_val" id="mem_util_prog_bar_val">38 %</div>
</td>
</tr>


</tbody>
</table>
</div> <!-- fp_sub_container -->

<div id="page_buttons" class="fp_button_row">
<input class="fp_button ui-button ui-widget ui-state-default" type="submit" id="b_form1_submit" name="b_form1_submit" value="Apply" onclick="jslib_b_pressed_g='submit';">
&nbsp;
<input class="fp_button ui-button ui-widget ui-state-default" type="submit" id="b_form1_refresh" name="b_form1_refresh" value="Refresh" onclick="jslib_b_pressed_g='refresh';">
&nbsp;
<input class="fp_button ui-button ui-widget ui-state-default" type="reset" id="b_form1_cancel" name="b_form1_cancel" value="Cancel" onclick="jslib_b_pressed_g='cancel';">
</div> <!-- fp_button_row -->
</form> <!-- form1 -->

</div><!-- fp_page_container -->

<script type="text/javascript" language="JavaScript">
<!--
  var jslib_msgs = parent.jslib_msgs_tbl;
-->
</script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/js/web-utils-combo.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/plugins/jquery-plugins-combo.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/datatables_1_9_4/jquery.dataTables-plugins.js"></script>
<script type="text/javascript" src="/htdocs/lang/en_us/culture/globalize.culture.en-US.20120606.js"></script>
<script type="text/javascript" src="/htdocs/static/bt1671095783/jquery/jquery_ui_1_12_1/jquery-ui-1.12.1.min.js"></script>

<script type="text/javascript" language="JavaScript">
<!--


// Construct property objects for each input field in the form
var prop =
{
  sys_location: new FieldProp({ defval: "", dname: "System Location", formfield: "sys_location", max: 255, min: 0, optional: true, regex: /^[ -~]+$/, type: 2 }),
  sys_name: new FieldProp({ defval: "", dname: "System Name", formfield: "sys_name", max: 64, min: 0, optional: true, regex: /^[ -~]+$/, type: 2 }),
  sys_contact: new FieldProp({ defval: "", dname: "System Contact", formfield: "sys_contact", max: 255, min: 0, optional: true, regex: /^[ -~]+$/, type: 2 })
};

jslib_form_validation_bind($('#form1')[0], prop);

prop.sys_contact.uservalidate = function(field)
{
  // This is a simple example of doing user validation.  In actuality,
  // it does not do anything (just passes through the value.)
  var re = /^./ ;

  if (field.value.length > 0 && !re.test(field.value))
  {
    return { errmsg: jsmsg.invalid_chars };
  } else {
    return null;
  }
}

$(function()
{
  $("div .fp_progressbar").each(function()
  {
    var sel = "#" + this.id;
    var val = elem_get(this.id + "_val").innerHTML;
    $(sel).progressbar({ value: val });
    $(sel).css({ "background": "#eeeeee" });
    $(sel + " > div").css({ "background": "green" });
  });
});

function progress_bar_update(id, val, lev1, lev2)
{
  var barcolor = "#00b388";
  if (lev1 != null)
  {
    ////lev1 = 101; lev2 = 0;
    // lev1 designates a two-color scheme
    barcolor = (val < lev1) ? "green" : "red";

    if ((lev2 != null) && (lev1 < lev2) && (val >= lev1))
    {
      // lev1 and lev2 designates a three-color scheme
      // (note: if specified, lev2 must be greater than lev1)
      barcolor = (val < lev2) ? "yellow" : "red";
    }
  }
  $(id).progressbar("option", "value", val);
  $(id + " > div").css({ "background": barcolor });
}

// define form field(s) to be updated through Ajax using the specified script file
//   - script must produce results in same order as those listed in the fields array
$(document).ready(function()
{

  progress_bar_update("#cpu_util_prog_bar", 32);
  progress_bar_update("#mem_util_prog_bar", 38);
  var fn = setInterval(function()
  {
    $.ajax(
    {
      url: "/htdocs/lua/ajax/dashboard_ajax.lua",
      success: function(val)
      {
        var res = val.split("|");
        if (res != null)
        {
          elem_get("sys_up_time").innerHTML = res[0];

          var cpu_util = Number(res[1]);
          elem_get("cpu_util_prog_bar_val").innerHTML = cpu_util + " %";
          progress_bar_update("#cpu_util_prog_bar", cpu_util);

          var mem_util = Number(res[2]);
          elem_get("mem_util_prog_bar_val").innerHTML = mem_util + " %";
          progress_bar_update("#mem_util_prog_bar", mem_util);
          elem_get("curr_time").innerHTML = res[3];
          elem_get("curr_date").innerHTML = res[4];
        }
      }
    });
  }, 60000);
});

-->
</script>

<script type="text/javascript" language="JavaScript">
<!--
$(document).ready( function()
{
  var page_is_valid = true;

  // format all culture-specific elements using the current locale
  culture_format(parent.culture);


    var myNav = navigator.userAgent.toLowerCase();
    var isIe = false;
    if (myNav.indexOf('msie') != -1)
    {
      var myVer = parseInt(myNav.split('msie')[1]);
    }

    if ((isIe == true) && (myVer < 8)) {
    $('input[type=radio],[type=checkbox]').live('click', function () {
      this.blur();
      this.focus();
    });
  }

  $(':input').bind('keypress', function(e) {
    var key = (window.event) ? window.event.keyCode : e.which;  // IE vs. FF
    var $this = $(this);
    if ( ($this.is(':not(:button, :submit, :reset, textarea)')) ) {
      return (key != 13);
    }
  });

  $(".fp_button").button();
    $(".fp_button_cancel").button();

  $('form input[type="reset"]').click(function(e) {
   if( $('#sorttable1').length ){
    fp_dt_reset_handler("#sorttable1");
   }
    return jslib_form_reset(this.form);
  });

  $(":submit,:button").click(function(e) {
    // remember which button was clicked last by storing into hidden field
    var button = $(this).attr("id");
    var form_id = $(e.target).closest("form").attr("id");
    if (form_id)
    {
      $("#b_"+form_id+"_clicked").val(button);
    }
    page_is_valid = jslib_form_validate(document.forms[0], prop);

    return page_is_valid;
  });

  // add a hidden field to each form to record which submit button
  // was clicked so that it gets presented in the POST data
  $("form").each(function() {
    var $this = $(this);
    var bid = "b_" + $this.attr("id") + "_clicked";
    var b_clicked = '<input type="hidden" id="' + bid + '" name="' + bid + '">';
    $(b_clicked).appendTo($this);
  });
  $(window).resize(function() {
    if(this.resizeTO) clearTimeout(this.resizeTO);
    this.resizeTO = setTimeout(function() {
      $(this).trigger('resizeEnd');
      }, 500);
  });
  $(window).bind('resizeEnd', function() {
      iframe_auto_resize();
  });
  iframe_auto_resize();
  $('form input[type="submit"]').click(function(e) {
    var form_id = $(e.target).closest("form").attr("id");
    var f_s = "b_"+form_id+"_submit";
    var f_r = "b_"+form_id+"_refresh";
    var f_click = $("#b_"+form_id+"_clicked").val();
    if (((f_click == f_s) || (f_click == f_r)) && page_is_valid)
    {
      parent.progress_modal_open();
    }
  });
  parent.progress_modal_handler(parent.ple.PAGE_LOADED);

  check_error();
  focus_init("");
});
-->
</script>

</body>
</html>
"""
