#!/usr/bin/perl
use CGI;
BEGIN{
  use CGI::Carp qw(carpout);
  open LOG,"/usr/lib/cgi-bin/table_error.log"
 or die "Couldn't open log file: $!";
while(<LOG>)
{
print LOG "$!";
}
  carpout(LOG);
}
my $q =new CGI;
print("content-type:text/html\n\n");
print $q->start_html('Register table'),
     $q->table({-border=>1},$q->Tr( [ $q->th([ "Registration no.", "Name", "Age", "Gender", "Graduation", "H/D" ] ),
      $q->td( [ $q->param('regno'), $q->param('name'), $q->param('age'), $q->param('gender'), $q->param('graduation'), $q->param('H/D')])])),$q->end_html;

