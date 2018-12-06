#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
$q=new CGI;
print $q->header(),
$q->start_html(),
$q->start_form(-name=>sequpdate, -method=>post, -action=>"http://127.0.0.1/cgi-bin/proupdate_process.cgi"),
"<br>Protein name : ",
$q->textfield(-name=>proname),
"<br>Update the sequence:",
$q->textarea(-name=>seq,-rows=>10,-cols=>50),
$q->submit(-label=>Submit),
$q->end_form(),
$q->end_html();
