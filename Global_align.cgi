#!/usr/bin/perl
use CGI;
use CGI::Carp qw(fatalsToBrowser);
$q= new CGI;
print $q->header();
print "<br><br>";
$fasta1 = $q->param('FASTA1');
while($line1=<$fasta1>)
{
	next if($line1=~/>.*/ig);
	$seq1=$seq1.$line1;
}
$fasta2 = $q->param('FASTA2');
while($line2=<$fasta2>)
{
	next if($line2=~/>.*/ig);
	$seq2=$seq2.$line2;
} 
$fasta2 = $q->param('FASTA2'); 
my $match = 2;
my $mismatch = -1; 
my $gap = -2;
print "==============================<br>" ;
print "=======GLOBAL ALIGNMENT========<br>" ;
print "==============================<br>" ; 
$seq1 = join('',split(/\n/, $seq1));
$seq2 = join('',split(/\n/, $seq2));

# scoring scheme
my $MATCH    =  1; # +1 for letters that match
my $MISMATCH = -1; # -1 for letters that mismatch
my $GAP      = -1; # -1 for any gap

# initialization	
my @matrix;
$matrix[0][0]{score}   = 0;
$matrix[0][0]{pointer} = "none";
for (my $j = 1; $j <= length($seq1); $j++) {
    $matrix[0][$j]{score}   = $GAP * $j;
    $matrix[0][$j]{pointer} = "left";
}
for (my $i = 1; $i <= length($seq2); $i++) {
    $matrix[$i][0]{score}   = $GAP * $i;
    $matrix[$i][0]{pointer} = "up";
}

# fill
for (my $i = 1; $i <= length($seq2); $i++) {
    for (my $j = 1; $j <= length($seq1); $j++) {
        my ($diagonal_score, $left_score, $up_score);

        # calculate match score
        my $letter1 = substr($seq1, $j-1, 1);
        my $letter2 = substr($seq2, $i-1, 1);                            
        if ($letter1 eq $letter2) {
            $diagonal_score = $matrix[$i-1][$j-1]{score} + $MATCH;
        }
        else {
            $diagonal_score = $matrix[$i-1][$j-1]{score} + $MISMATCH;
        }

        # calculate gap scores
        $up_score   = $matrix[$i-1][$j]{score} + $GAP;
        $left_score = $matrix[$i][$j-1]{score} + $GAP;

        # choose best score
        if ($diagonal_score >= $up_score) {
            if ($diagonal_score >= $left_score) {
                $matrix[$i][$j]{score}   = $diagonal_score;
                $matrix[$i][$j]{pointer} = "diagonal";
            }
	    else {
                $matrix[$i][$j]{score}   = $left_score;
                $matrix[$i][$j]{pointer} = "left";
            }
        } 
        else {
            if ($up_score >= $left_score) {
                $matrix[$i][$j]{score}   = $up_score;
                $matrix[$i][$j]{pointer} = "up";
            }
            else {
                $matrix[$i][$j]{score}   = $left_score;
                $matrix[$i][$j]{pointer} = "left";
            }
        }
    }
}

# trace-back

my $align1 = "";
my $align2 = "";

# start at last cell of matrix
my $j = length($seq1);
my $i = length($seq2);

while (1) {
    last if $matrix[$i][$j]{pointer} eq "none"; # ends at first cell of matrix

    if ($matrix[$i][$j]{pointer} eq "diagonal") {
        $align1 .= substr($seq1, $j-1, 1);
        $align2 .= substr($seq2, $i-1, 1);
        $i--;
        $j--;
    }
    elsif ($matrix[$i][$j]{pointer} eq "left") {
        $align1 .= substr($seq1, $j-1, 1);
        $align2 .= "-";
        $j--;
    }
    elsif ($matrix[$i][$j]{pointer} eq "up") {
        $align1 .= "-";
        $align2 .= substr($seq2, $i-1, 1);
        $i--;
    }    
}

$align1 = reverse $align1;
$align2 = reverse $align2;
@a = split(//,$align1) ; 
@b = split(//,$align2) ;
$len = @a ; 
$sum = 0 ; 
$j = 0 ; 
$nomatch = 0 ; 
$nomismatch = 0 ; 
$nogap = 0 ; 
for ($i= 0; $i<$len; $i++) 
{
while ($i==$j)
 {
if ($a[$i] eq $b[$i]) 
{
$sum = $sum+$MATCH ; 
$nomatch = $nomatch+1;
print "Match : $a[$i] -- $b[$i] Match no: $nomatch<br>"
 }
elsif (($a[$i] eq "-" )||( $b[$i] eq "-")) 
{
$sum = $sum + $GAP ;
$nogap = $nogap + 1 ;
print "Gap : $a[$i] -- $b[$i] Gap no: $nogap<br>"
 }
else 
{
$sum = $sum + $MISMATCH ;
$nomismatch = $nomismatch + 1 ;
print "Mismatch : $a[$i] -- $b[$i] Mismatch no: $nomismatch<br>"
}
$j++ ;
 }
}
print "<br>";
print " Score : $sum <br>";
print " Matches : $nomatch <br>"; 
print " Mismatches : $nomismatch <br>"; 
print " Gaps : $nogap <br>"; 
#print "$align1<br>";
#print "$align2<br>";
print "==============================<br>";

