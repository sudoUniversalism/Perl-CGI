#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
$q=new CGI;
print $q->header(),
$q->start_html(),
"<h2>Protein database</h2>",
$q->a({-href=>"db.cgi"},"Enter data"),"<br>",
$q->a({-href=>"proquery.cgi"},"Retrieve data"),"<br>",
$q->a({-href=>"proupdate.cgi"},"Update data"),"<br>",
$q->end_html();
