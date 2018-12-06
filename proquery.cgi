#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
$q=new CGI;
print $q->header(),
$q->start_html(),
$q->start_form(-name=>proteinquery, -method=>post, -action=>"http://127.0.0.1/cgi-bin/proquery_process.cgi"),
"<br>Protein name/id : ",
$q->textfield(-name=>'proname'),
$q->submit,
$q->end_form(),
$q->end_html();

