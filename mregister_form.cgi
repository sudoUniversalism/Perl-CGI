#!/usr/bin/perl
use CGI;
BEGIN
{
use CGI::Carp qw(carpout);
open (LOG,">>/usr/lib/cgi-bin/reg_error.log") or die ("couldnt write the log: $!");
while(<LOG>)
{
print "$!";
}
carpout(LOG);
}
$q=new CGI;
print $q->header();
print $q->start_html(),
$q->center($q->h1('Registration Form')),
"<br>",
$q->start_form(-name=>myform, -method=>post, -action=>"http://127.0.0.1/cgi-bin/mtable_form.cgi"),
"Register Number :",
$q->textfield('rn'),
"<br>",
"Name :",
$q->textfield('name'),
"<br>",
"Age :",
$q->textfield('age'),
"<br>",
"Gender :",
$q->radio_group(-name=>'gender', -values=>["Male","Female"], -labels=>{Male=>"Male",Female=>"Female"}),
"<br>",
"Highest qualification :",
$q->popup_menu(-name=>'hq', -values=>["UG","PG","Phd"], -labels=>{UG=>"Under Graduate",PG=>"Post Graduate",Phd=>"Doctorate of Philosophy"}),
"<br>",
"Preference :",
$q->checkbox_group(-name=>'pf', -values=>["Biotechnology","Microbiology","Bioinformatics"]),
"<br>",
"Opinion about the course selected :<br>",
$q->textarea(-name=>'op', -rows=>"10", -cols=>"30"),
"<br>",
"Hostler / Day-Scholar :",
$q->radio_group(-name=>'hd', -values=>["Hostler","Day-Scholar"], -labels=>{Hostler=>"Hostler",Day-Scholar=>"Day-Scholar"}),
"<br> <br>",
$q->center($q->submit("Submit")),
$q->end_form(),
$q->end_html();



