<?php
function _loaddb()
{
	$fdata['actionUrl'] = myUrl('ops/loaddb');
	$fdata['cancelUrl'] = myUrl('mgmt_main/index');
 	$data['pagename']='Load Database';
  $data['body'][]='<h2>Warning Submitting this form will replace all existing data the Database</h2><br/>';
  $data['body'][]=View::do_fetch(VIEW_PATH.'mgmt_main/loaddb.php', $fdata); 
  View::do_dump(VIEW_PATH.'layouts/mgmtlayout.php',$data);

}