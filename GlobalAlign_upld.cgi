#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q=new CGI;
print $q->header();
print $q->start_html('GLOBAL ALIGNMENT INTERFACE'),
$q->h3($q->i('GLOBAL ALIGNMENT')),
$q->start_form(-name=>'myform',-action=>'Global_align.cgi',-method=>'post',-enctype=>'multipart/form-data'),
"Upload first sequence as FASTA file :",$q->filefield('FASTA1'),"<br><br>",
"Upload first sequence as FASTA file :",$q->filefield('FASTA2'),"<br><br>",
$q->submit,$q->end_form,$q->end_html();
