#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
my $q=new CGI;
print("Content-type:text/html\n\n");
print $q->start_html(),
 $q->h1('Upload form'),
    $q->start_form(-name=>'myform' ,-action=>'http://127.0.0.1/cgi-bin/process_file.cgi',-method=>'post', enctype=>"multipart/form-data"),
"INPUT SEQUENCE TO BE STORED:",$q->textfield('storeseq'),"<br>","<br>",
"QUERY SEQUENCE TO BE SEARCHED:",$q->textfield('fseq'),"<br>","<br>",
"FASTA FILE:",$q->filefield(-name=>'file'),
$q->submit,
$q->end_html(); 
