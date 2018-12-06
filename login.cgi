#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q=new CGI;
print $q->header;
print $q->start_html();
print $q->start_form(-name=>"myform",-action=>"mylogin_bypm.cgi",-method=>'post');
print "Username:",$q->textfield('userid'),"<br>";
print "Password:",$q->textfield('pass'),"<br>";
print $q->submit;
print $q->end_html;
