#!/usr/bin/perl
use CGI;
BEGIN{
  use CGI::Carp qw(carpout fatalsToBrowser);
  open (LOG,">>/usr/lib/cgi-bin/register_error.log")
 or die ("Couldn't open log file: $!");
while(<LOG>)
{
print LOG "$!";
}
  carpout(LOG);
}
my   $q=new CGI;
print("content-type:text/html\n\n");
print $q->start_html(),
    $q->h1('Registration form'),
    $q->start_form(-name=>'myform' ,-action=>'http://127.0.0.1/cgi-bin/table_form.cgi',-method=>'post'),
    "Register No:",$q->textfield('regno'),"<br>",
    "Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:",$q->textfield('name'),"<br>",
    "Age&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:",$q->textfield('age'),"<br>",
    "Gender",$q->radio_group(-name=>"gender",-values=>["Male","Female"],-labels=>{Male=>"Male",Female=>"Female"}),"<br>",
    "Graduation:",$q->popup_menu(-name=>'graduation',-values=>['UG','PG','Phd']),"<br>",  
"Preference:",$q->checkbox_group(-name=>"preferences",-values=>['Microbiology','Biotechnology','Bioinformatics']),"<br>",
"Opinion about course:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",$q->textarea(-name=>'opinion',-rows=>10,-cols=>30),"<br>",
 "Hostler/Day-scholar:",$q->radio_group(-name=>'H/D',-values=>['Hostler','Day-scholar'],-labels=>{Hostler=>"Hostler",Day-scholar=>"Day-scholar"}),"<br>",
    $q->p,
    $q->submit,
    $q->end_form();
