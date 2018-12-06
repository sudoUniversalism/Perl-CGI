#!/usr/bin/perl
print "content-type:text/html\n\n";
$method=$ENV{REQUEST_METHOD};
if($method eq "GET")
	{
		$data=$ENV{QUERY_STRING};
#print "get:$data";
	}

if($method eq "POST")
	{
		$data = <STDIN>;
#print "post:$data";
	}

@kv=split(/&/,$data);
@u=split(/=/,$kv[0]);
@p=split(/=/,$kv[1]);
$user=$u[1];
$pw=$p[1];
if ($user eq "amma" && $pw eq "1234")
	{
		print $q->start_html;
		print"<h3>Login Successfull</h3><br>";
		print $q->a({-href=>"http://127.0.0.1/cgi-bin/mylogin_bypm.cgi"},"Login using CGI.pm");
	}
else
	{
		print $q->start_html;
		print"<h3>Invalid User</h3><br>";
		print $q->a({-href=>"http://127.0.0.1/cgi-bin/mylogin_bypm.cgi"},"Login using CGI.pm");
	}


