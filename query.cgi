#!/usr/bin/perl
use CGI;
$q=new CGI;
print $q->header();
$seq=$q->param('queryseq');
if($seq!~/[ATCG]+$/gi)
{
print "invalid sequence";
exit;
}

$filename=$q->param('dna');
print "$filename<br>";
while($line=<$filename>)
{
next if($line=~/^>/);
$fileseq=$fileseq.$line;
}

if($fileseq=~/$seq/ig){
print "query found";
}
else{
print "query sequence not found";
}
