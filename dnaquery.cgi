#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header(),
$q->start_html(-title=>'DNA search'),
$q->h2('Sequence Search'),
$q->start_form(-name=>query, -method=>post, -action=>"http://127.0.0.1/cgi-bin/query.cgi", enctype=>"multipart/form-data"),
"<br>Enter your Query Sequence",
$q->textfield(-name=>queryseq),
"<br><br>Upload your file",
$q->filefield(-name=>dna),
"<br><br>",
$q->submit(),
$q->end_form(),
$q->end_html();


