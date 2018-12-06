#!/usr/bin/perl
use CGI;
use CGI::Carp qw (fatalsToBrowser);
use DBI;
$q=new CGI;
print $q->header();
$name=$q->param(proname);
$seq=$q->param(seq);
$bond=$q->param(bond);
$msite=$q->param(motsite);
$mname=$q->param(motname);
$org=$q->param(organism);
$dbh=DBI->connect('dbi:mysql:proteindb','root','password');
$rows =$dbh->do ("insert into protein_details values('$name','$seq','$bond','$msite','$mname','$org')") || die ("Could not Insert record: $DBI::errstr<br>");
print "$rows row added to the table<br>";

$sth=$dbh->prepare("select * from protein_details")or die;
$sth->execute();
while(my @row = $sth->fetchrow_array)
 {
    print "@row<br>"
 }
