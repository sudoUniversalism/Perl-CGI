#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header(),
$q->start_html('ORF FINDER'),
$q->i('ORF FINDER'),"<br><br>",
$q->start_form(-name=>'myform',-action=>'orf.cgi',-method=>'post',-ecntype=>'mutipart/form-data'),
$q->filefield(-name=>'myfile'),"<br><br>",
$q->submit(),
$q->end_form(),
$q->end_html();
