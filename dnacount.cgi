#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header();
$filename=$q->param('filename');
$seq=$q->param('dnaseq');
if($seq!~/[ATCG]+$/gi)
{
print "Invalid sequence";
exit;
}
open (DNA,">/usr/lib/cgi-bin/$filename") or die "$!";
print DNA $seq;
print "<h3>DNA sequence successfully stored to a file!</h3>";
$a=$seq=~tr/[Aa]//;
$t=$seq=~tr/[Tt]//;
$g=$seq=~tr/[Gg]//;
$c=$seq=~tr/[Cc]//;
print "<h4>Count of bases</h4>Adenine:$a<br>Thimine:$t<br>Guanine:$g<br>Cytosine:$c<br>";
