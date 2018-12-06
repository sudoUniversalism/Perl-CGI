#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Bio::Tools::Run::StandAloneBlastPlus;
$fac=Bio::Tools::Run::StandAloneBlastPlus->new(-db_name=>'pdb');
$q=new CGI;
print $q->header();
$filename=$q->param('file');
while($line=<$filename>){
next if($line=~/>.*+$/ig);
$string=$string.$line;
}
$sites=$q->param('sites');
$string=~s/$sites/--$sites--/ig;
print $q->start_html('BINDING SITES'),
print "$string<br>";
$fac->bl2seq( -method => 'blastp',
              -query => $seq);
$result = $fac->blastn( -query => $seq,
                        -outfile => 'query.bls');
