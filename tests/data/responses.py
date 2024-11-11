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
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_2" value="2"><label></label>', '2', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_3" value="3"><label></label>', '3', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_4" value="4"><label></label>', '4', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Delivering Power', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_5" value="5"><label></label>', '5', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_6" value="6"><label></label>', '6', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_7" value="7"><label></label>', '7', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Delivering Power', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_8" value="8"><label></label>', '8', 'Disabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Disabled', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_9" value="9"><label></label>', '9', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Searching', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_10" value="10"><label></label>', '10', 'Enabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Delivering Power', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_11" value="11"><label></label>', '11', 'Disabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Disabled', 'None', 'nil']
,
['<input type="checkbox" class="chkrow" name="chkrow[]" id="chkrow_12" value="12"><label></label>', '12', 'Disabled', 'None', 'None', 'Disabled', 'Dot3af/at', 'Class', 'Disabled', 'None', 'nil']
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
