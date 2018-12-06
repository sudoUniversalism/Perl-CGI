#!/usr/bin/perl
use CGI;
use CGI qw(fatalsToBrowser);
$q=new CGI;
print header();
foreach (param) {
print "Parameter $_ is \n";
print param($_);
}
