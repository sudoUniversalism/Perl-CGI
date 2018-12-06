#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Bio::AlignIO; 
use Bio::Align::ProteinStatistics; 
use Bio::Tree::DistanceFactory; 
use Bio::TreeIO; 
use Bio::Tree::Draw::Cladogram;
$q=new CGI;
print $q->header();
$filename=$q->param('myfile');
print "$filename";
open(NEW,">http://127.0.0.1/cgi-bin/$filename") or die "Cannot upload file: $!";
while($line=<$filename>){
print NEW "$line\n";
}
carpout(NEW);
my $alnio = Bio::AlignIO->new(-file => $filename, -format=>'fasta');
my $dfactory = Bio::Tree::DistanceFactory->new(-method => 'NJ');
my $stats = Bio::Align::ProteinStatistics->new;
my $treeout = Bio::TreeIO->new(-format => 'newick');
while( my $aln = $alnio->next_aln ) 
{
my $mat = $stats->distance(-method => 'Kimura',
                           -align  => $aln);
my $tree = $dfactory->make_tree($mat);
$treeout->write_tree($tree);
}
my $t1 = $treeout->next_tree;
my $t2 = $treeout->next_tree;
 
my $obj1 = Bio::Tree::Draw::Cladogram->new(-tree => $t1);
$obj1->print(-file => 'cladogram.eps');
 
if ($t2) {
  my $obj2 = Bio::Tree::Draw::Cladogram->new(-tree => $t1, -second => $t2);
  $obj2->print(-file => 'tanglegram.eps');
}
