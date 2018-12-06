#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header(),
$q->start_html(-title=>'DNA upload'),
$q->h2('Enter your DNA Sequence'),
$q->start_form(-name=>dna, -method=>post, -action=>"http://127.0.0.1/cgi-bin/dnacount.cgi"),
$q->textarea(-name=>dnaseq, -rows=>20, -cols=>100),
"<br><br>Enter a filename to store the sequence:",
$q->textfield(-name=>filename),
"<br><br>",
$q->submit(-value=>Submit),
$q->end_form(),
$q->end_html();

