#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use DBI;
$q=new CGI;
print $q->header();
$dbh=DBI->connect('dbi:mysql:proteindb','root','password');
$name=$q->param('proname');
$sth=$dbh->prepare("select * from protein_details where proteinID='$name'")or die;
$sth->execute();
@row=$sth->fetchrow_array();
print "Protein name: $row[0]<br>sequence: $row[1]
<br>Bond type: $row[2]<br>motif site: $row[3]
<br>motif name: $row[4]<br>organism: $row[5]";

