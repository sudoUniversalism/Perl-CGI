#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Bio::Tools::Run::StandAloneBlastPlus;
$q=new CGI;
$fac = Bio::Tools::Run::StandAloneBlastPlus->new(
  -db_name => 'pdb');
print $q->header();
$file=$q->param('myfile');
while($line=<$file>)
{
next if($line=~/>.*/ig);
$seq=$seq.$line;
}
$seq2=uc $seq;
$seq3=uc $seq;
$seq4=uc reverse($seq);
$seq5=uc reverse($seq);
$seq6=uc reverse($seq);
%aa= ("TTT" => " F ", "TTC" => " F ", "TTA" => " L ", "TTG" => " L ",
  "TCT" => " S ", "TCC" => " S ", "TCA" => " S ", "TCG" => " S ",
  "TAT" => " Y ", "TAC" => " Y ", "TAA" => " (STOP) ", "TAG" => " STOP ",
  "TGT" => " C ", "TGC" => " C ", "TGA" => " (STOP) ", "TGG" => " W ",
  "CTT" => " L ", "CTC" => " L ", "CTA" => " L ", "CTG" => " L ",
  "CCT" => " P ", "CCC" => " P ", "CCA" => " P ", "CCG" => " P ",
  "CAT" => " H ", "CAC" => " H ", "CAA" => " Q ", "CAG" => " Q ",
  "CGT" => " R ", "CGC" => " R ", "CGA" => " R ", "CGG" => " R ",
  "ATT" => " I ", "ATC" => " I ", "ATA" => " I ", "ATG" => " M(START) ",
  "ACT" => " T ", "ACC" => " T ", "ACA" => " T ", "ACG" => " T ",
  "AAT" => " N ", "AAC" => " N ", "AAA" => " K ", "AAG" => " K ",
  "AGT" => " S ", "AGC" => " S ", "AGA" => " R ", "AGG" => " R ",
  "GTT" => " V ", "GTC" => " V ", "GTA" => " V ", "GTG" => " V ",
  "GCT" => " A ", "GCC" => " A ", "GCA" => " A ", "GCG" => " A ",
  "GAT" => " D ", "GAC" => " D ", "GAA" => " E ", "GAG" => " E ",
  "GGT" => " G ", "GGC" => " G ", "GGA" => " G ", "GGG" => " G ",
);
$seq= uc $seq;
$length=length($seq);
$codon_l=$length/3;
$cut=0;
for($i=0;$i<$codon_l;$i++)
{
$codons[$i]=substr($seq,$cut,3);
$cut+=3;
}
$cut=1;
for($i=0;$i<$codon_l;$i++)
{
$codons2[$i]=substr($seq2,$cut,3);
$cut+=3;
}
$cut=2;
for($i=0;$i<$codon_l;$i++)
{
$codons3[$i]=substr($seq3,$cut,3);
$cut+=3;
}
$cut=0;
for($i=0;$i<$codon_l;$i++)
{
$codons4[$i]=substr($seq4,$cut,3);
$cut+=3;
}
$cut=1;
for($i=0;$i<$codon_l;$i++)
{
$codons5[$i]=substr($seq5,$cut,3);
$cut+=3;
}
$cut=2;
for($i=0;$i<$codon_l;$i++)
{
$codons6[$i]=substr($seq6,$cut,3);
$cut+=3;
}
$length_arr=$#codons+1;
print"+1 FRAME: @codons<br>";
print"+2 FRAME: @codons2<br>";
print"+3 FRAME: @codons3<br>";
print"-1 FRAME: @codons4<br>";
print"-2 FRAME: @codons5<br>";
print"-3 FRAME: @codons6<br>";
print"Amino acid sequence of corresponding +1 sequence is : <br>";
for($i=0;$i<=$length_arr;$i++)
{
if(length($codons[$i])==3)
{
print"$aa{$codons[$i]} ";
}
}
print"<br>Amino acid sequence of corresponding +2 sequence is : <br>";
for($i=0;$i<=$length_arr;$i++)
{
if(length($codons2[$i])==3)
{
print"$aa{$codons2[$i]} ";
}
}
print"<br>Amino acid sequence of corresponding +3 sequence is : <br>";
for($i=0;$i<=$length_arr;$i++)
{
if(length($codons3[$i])==3)
{
print"$aa{$codons3[$i]} ";
}
}
print"<br>Amino acid sequence of corresponding -1 sequence is : <br>";
for($i=0;$i<=$length_arr;$i++)
{
if(length($codons4[$i])==3)
{
print"$aa{$codons4[$i]} ";
}
}
print"<br>Amino acid sequence of corresponding -2 sequence is : <br>";
for($i=0;$i<=$length_arr;$i++)
{
if(length($codons5[$i])==3)
{
print"$aa{$codons5[$i]} ";
}
}
print"<br>Amino acid sequence of corresponding -3 sequence is : <br>";
for($i=0;$i<=$length_arr;$i++)
{
if(length($codons6[$i])==3)
{
print"$aa{$codons6[$i]} ";
}
print"\n";
}
print"<br>";
$fac->bl2seq( -method => 'blastp',
              -query => $seq);
$result = $fac->blastn( -query => 'query_seqs.fas',
                        -outfile => 'query.bls');









