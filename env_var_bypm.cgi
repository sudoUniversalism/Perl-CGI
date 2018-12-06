#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header();


print"<h2>Environment variables</h5><br>";
foreach(sort($q->http))
 {
print "$_:";
print "  ",$q->http($_),"<br>";
}
print $q->start_html,
$q->a({-href=>"http://127.0.0.1/cgi-bin/env_var.cgi"},"Without CGI"),
$q->end_html;
