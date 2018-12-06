#!/usr/bin/perl 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
 my $q= new CGI;
 # if no parameters are send: means the form is not submitted
 
unless ($q->param)   
{
my $ifcookie = $q->cookie('mycookie');
my $ifcookie2= $q->cookie('mycookie2');
	if($ifcookie && $ifcookie2)                         #if cookie exist
	{
 	print $q->header;
  	print $q->start_html(); 
  	print "Amino acid chosen earlier was $ifcookie<br>frequency: $ifcookie2";
  print	$q->start_form(-name=>mf, -method=>post, -action=>"http://127.0.0.1/cgi-bin/cookie_self.cgi");
print "Select amino acid :";
print $q->popup_menu(-name=>aa, -values=>[qw(Glycine Valine Alanine Leucine Isoleucine Proline Phenylalanine Tyrosine Tryptophan Serine Threonine Cystine Methionine Asparagine Glutamine Lysine Arginine Histidine Aspartate Glutamate)], -default=>"$ifcookie");
print "Enter the required Frequency of the selected amino acid :";
print $q->textfield(-name=>tf, -default=>"$ifcookie2");
print "<br>";
$q->submit();
$q->end_form();
  	print $q->end_html;
	}

        else
	{	
          print $q->header;
          print $q->start_html("Cookie");

          print "<FORM action = http://127.0.0.1/cgi-bin/cookie_pgm.cgi method = post>";
 
          print "Select an amino acid :";
print $q->popup_menu(-name=>aa, -values=>[qw(Glycine Valine Alanine Leucine Isoleucine Proline Phenylalanine Tyrosine Tryptophan Serine Threonine Cystine Methionine Asparagine Glutamine Lysine Arginine Histidine Aspartate Glutamate)]);
print "<br>Enter the Frequency:";
print $q->textfield(-name=>tf);
print "<br>";
          print $q->submit;
          print $q->end_form;
           print $q->end_html;
         }
}
else 
                                  # the form is submitted
{
my $cid = $q->param(aa);
my $cid2= $q->param(tf);
my $cook = $q->cookie(-name=>'mycookie', -value=>"$cid", -expires=>'+2h');
my $cook2 = $q->cookie(-name=>'mycookie2', -value=>"$cid2", -expires=>'+2h');

print $q->header(-cookie=>[$cook,$cook2]);
print "cookie is created. <br>Amino acid : $cid <br>Frequency: $cid2";
print $q->end_html;
}


