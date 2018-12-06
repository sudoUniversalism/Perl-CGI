#!/usr/bin/perl 
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use DBI;
$q=new CGI;
print "Content-type: text/html\n\n"; 
$protein=$q->param('protein');
$sequence=$q->param('seq');
$bond=$q->param('bond');
$organism=$q->param('Organism');
$motif_site=$q->param('Motif_site');
$motif_name=$q->param('Motif_name');    
$user= "root";
$password = "password";
$dbh = DBI->connect("dbi:MySQL:proteindb;localhost", $user, $password);
$query = $dbh->prepare("insert into protein_details values($protein,$sequence,$bond,$organism,$motif_site,$motif_name)");
$query->execute();
#while(my @result = $query->fetchrow_array)
    print "$query";
    print $q->br;
$dbh->disconnect_all;

