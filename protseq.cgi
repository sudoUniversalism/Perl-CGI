#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header(),
$q->start_html(-title=>'protein sequence'),
$q->h2('Enter your Protein Sequence'),
$q->start_form(-name=>prot, -method=>post, -action=>"http://127.0.0.1/cgi-bin/protcount.cgi"),
$q->textarea(-name=>protseq, -rows=>20, -cols=>100),
"<br><br>Enter a filename to store the sequence:",
$q->textfield(-name=>filename),
"<br><br>",
$q->submit(-value=>Submit),
$q->end_form(),
$q->end_html();

