#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
$q=new CGI;
print $q->header(),
$q->start_html(-title=>'enter data'),"<h2>Enter the protein details</h2>",
$q->start_form(-name=>protein, -method=>post, -action=>"http://127.0.0.1/cgi-bin/dbinsert.cgi"),
"<br>Protein name : ",$q->textfield(-name=>proname),
"<br>sequence:<br>",$q->textarea(-name=>seq,-rows=>10,-cols=>50),
"<br>Bond type : ",$q->textfield(-name=>bond),
"<br>motif site:",$q->textfield(-name=>motsite),
"<br>motif name:",$q->textfield(-name=>motname),
"<br>organism:",$q->textfield(-name=>organism),
"<br><br>",$q->submit(-label=>'Submit Protein'),
$q->end_form(),
$q->end_html();







