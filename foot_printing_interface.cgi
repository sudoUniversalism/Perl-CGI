#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q=new CGI;
print $q->header();
print $q->start_html('DNA foot printing'),
$q->h3('DNA specificity finder'),
$q->start_form(-name=>'myform',-action=>'http://127.0.0.1/cgi-bin/footprinting.cgi'),
"Enter DNA in fasta format",$q->filefield('file'),
"Enter binding site:",$q->textfield('sites'),
$q->submit(),$q->end_form(),$q->end_html();

