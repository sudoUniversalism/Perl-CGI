#!/usr/bin/perl
use CGI;
$q=new CGI;
print $q->header;
$user=$q->param('userid');
$pw=$q->param('pass');
if ($user eq "amma" && $pw eq "1234")
	{
		print"<h3>Login Successfull</h3>";
	}
else
	{
		print"<h3>Invalid User</h3>";
	}

