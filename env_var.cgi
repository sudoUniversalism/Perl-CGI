#!/usr/bin/perl
print "content-type:text/html\n\n";
print"<h2>Environment variables</h5><br>";
foreach $key(sort keys(%ENV))
{
	print "$key: $ENV{$key}";
	print"<br><br>";
}
