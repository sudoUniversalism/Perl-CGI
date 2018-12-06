#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header();
$filename=$q->param('filename');
$seq=$q->param('protseq');
$seq=uc($seq);
	$seq=~tr/BJOUXZ//d;			#removing the unwanted characters
	$len=$seq=~tr/A-Z//;			#finding total length
	$total=$total+$len;
	$count=$seq=~tr/AILMFPWV//;		#counting hydrophobic aa
	$phobic=$phobic+$count;
	$percent=($phobic/$total)*100;

print "<h3>Protein Sequence successfully stored to file!</h3>$seq<br><br>Percentage of Hydrophobic Aminoacid: $percent%<br><br>";

open(PROTEIN,">/usr/lib/cgi-bin/$filename") or die "$!";
print PROTEIN $seq;
print PROTEIN "\nNumber of Hydrophobic Aminoacid:$phobic\nTotal length of protein sequence:$total\nPercentage of Hydrophobic Aminoacid: $percent%\n\n";

