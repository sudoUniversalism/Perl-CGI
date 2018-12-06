#!/usr/bin/perl

use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
our $q = new CGI;
unless($q->param())
{
  showform();
}
else
{
 
 showpage();
}

sub showform()
{
  print $q->header;
  print $q->start_html('login form'),
        $q->start_form,"Username : ",
        $q->textfield(-name=>'username'),
        $q->br,"Password : ",
        $q->textfield(-name=>'password'),
        $q->br,
        $q->submit(-value => login),
        $q->end_form,
        $q->end_html;

}
sub showpage()
{
 $sess = new CGI::Session("driver:FILE",undef,{Directory=>"/tmp"});
  $id = $sess->id();
   # to save data in session
   $sess->param("name",$q->param(username),"pass",$q->param(password));
   $s = $sess->param('name');
     # Create cookie and store session data
  
  my $cook= $q->cookie(-name=>'sessionid',
                      -value=>$id,-expires=>'+4d');
  print $q->header(-cookie=>[$cook]);
   print $q->br,
         $q->h3("Your data stored in the session is : Username: $s");
  print "<h3> Session Created <br> Session ID generated is $id</h3>";
  print $q->a({-href=>"http://127.0.0.1/cgi-bin/self.cgi"},"continue..");        
   print $q->start_form(-method=>"post",-action=>"http://127.0.0.1/cgi-bin/self.cgi"),
  "<br>", 
   $q->submit(-value=>'logout',-name=>'Submit');
   print $q->end_form(); 
        
}


