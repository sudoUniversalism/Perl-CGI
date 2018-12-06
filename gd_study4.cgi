#!/usr/bin/perl
use CGI;
use GD;
use GD::Graph::lines;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
$q=new CGI;
print "Content-type: image/jpeg\n\n";
@data=(["1st","2nd","3rd","4th","5th","6th","7th","8th","9th"], [1,2,5,6,3,1.5,1,3,4]);
$graph=GD::Graph::lines->new(400,300);
$graph->set(
x_label=>'X axis',
y_label=>'Y axis',
title=>'Simple Graph')
or die $graph->error;
$gd=$graph->plot(\@data) or die $graph->error;
open(PIC,">file3.jpeg") or die;
binmode PIC;
print $img_data->jpeg;
close PIC;
