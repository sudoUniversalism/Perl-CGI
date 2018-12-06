#!/usr/bin/perl
use CGI;
BEGIN
{
use CGI::Carp qw(fatalsToBrowser carpout);
open(LOG,">>/usr/lib/cgi-bin/table_error.log") or die("couldnot write to log : $!");
while(<LOG>)
{
print "$!";
}
carpout(LOG);
}
$q=new CGI;
print("Content-type:text/html\n\n");
print $q->start_html(),
$q->table({-border=>1}, $q->Tr([ $q->th(["Reg.No.","Name", "Age", "Gender", "Qualification", "H/D"]),
$q->td([ $q->param('rn'), $q->param('name'), $q->param('age'), $q->param('gender'), $q->param('hq'), $q->param('hd')])])),
$q->end_html(); 
