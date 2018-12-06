#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use DBI;
$q=new CGI;
print $q->header();
$dbh=DBI->connect('dbi:mysql:proteindb','root','password');
$name=$q->param(proname);
$seq=$q->param(seq);
$sth=$dbh->prepare("select * from protein_details where ProteinID='$name'")or die;
$rows =$dbh->do ("update protein_details set sequence='$seq' where ProteinID='$name';")|| die ("Could not Insert record: $DBI::errstr<br>");
print "$rows row updated to the table<br>";

$sth->execute();


