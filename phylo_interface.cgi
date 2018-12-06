#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q=new CGI;
print $q->header();
print $q->start_html(),
$q->start_form(-name=>'myform',-action=>'http://127.0.0.1/cgi-bin/Phylo_tree.cgi',-method=>'post',-enctype=>'multipart/form-data'),
"Upload newick file containing the sequences","<br><br>",$q->filefield('myfile'),"<br><br>"
,$q->submit(),$q->end_form,
$q->end_html();
