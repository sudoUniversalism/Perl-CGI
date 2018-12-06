#!/usr/bin/perl

use CGI;
use CGI::Session;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
our $q = new CGI;
#
#
$sid = $q->cookie('sessionid');
#
$session = new CGI::Session(undef,$sid,{Directory=>"/tmp"});
#
#
unless($q->param())
{
#
print $q->header;
print "from cookie: $sid";
$data = $session->param('name');
#
        if($data)
                {

print $q->header();
print $q->start_html(),"Inside Website",
$q->end_form,
$q->end_html();


                                print "<br> <h3>You are allowed to use the tool : Ur session id is </h3> ";

print ($session->id());
        print "<br><h3>Ur session data is: $data</h3>";

        }
}
else
{
print $q->header;
print "<h3>The session is going to be deleted...........";
if($q->param('Submit'))
 {

  destroyMe();
  }
  }
  sub destroyMe
  {
$session->delete();
 $sessid=$session->id('name');
  print "<br> The session is deleted: <br>Id is: $sessid<br>";
 
  
  }
 #
 #
