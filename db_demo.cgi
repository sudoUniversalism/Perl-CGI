#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use DBI;
$q=new CGI;
print $q->header();
$dbh=DBI->connect('dbi:mysql:proteindb','root','password');
$name="haemoglobin";
$sth=$dbh->prepare("select * from protein_details where proteinID='$name'")or die;
$sth->execute();
@row = $sth->fetchrow_array();
while(my @row = $sth->fetchrow_array)
 {
    print "@row<br>"
 }

