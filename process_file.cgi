#!/usr/bin/perl
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
my $q=new CGI;
print("Content-type:text/html\n\n");
my $filename=$q->param('file');
my $query=$q->param('fseq');
my $storestr=$q->param('storeseq');
while($line=<$filename>)
{
	my $line=~s/>.*/ /g;
	my $string.=$line;
}
if($query=~/[A|T|C|G|a|t|g|c]/ig)
	{
		if($string=~/.+$query.+/ig)
		{
			$string=~s/$query/*$query*/ig;
			print"Sequence found : $string<br>";	
		}
		else
		{
			print "Sequence not found\n\n";
		}
	}
	else
	{
		print "invalid query sequence\n\n";
	}
my $file="DNAstore.txt";
my $directory="/home/dell/Downloads"
open (STORE,">$directory/$file") or die("Unable to save your file.");
close STORE;
