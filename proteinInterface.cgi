#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
print "Content-type: text/html\n\n";
$q=new CGI;
print $q->start_html("PROTEIN INTERFACE"),
$q->start_form(-name=>"myform",-method=>"post",-action=>"DBI.cgi"),$q->h3($q->i("PROTEIN INTERFACE")),
"ENTER PROTEIN NAME",
$q->br,$q->textfield('protein'),
$q->br,$q->br,
"Enter protein sequence here:",
$q->br,
$q->textarea(-name=>'seq',-cols=>70,-rows=>5),
$q->br,$q->br,"Bond type:",
$q->br,$q->textfield('bond'),
$q->br,$q->br,"Organism:",
$q->br,$q->textfield('Organism'),
$q->br,$q->br,"Motif sites:",
$q->br,$q->textfield('Motif_site'),
$q->br,$q->br,"Motif names:",
$q->br,$q->textfield('Motif_name'),
$q->br,$q->br,$q->submit,$q->br,
$q->end_form,$q->end_html;
