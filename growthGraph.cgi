#!/usr/bin/perl
use CGI;
use GD::Graph::lines;
use strict;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
print ("Content-type: image/jpeg\n\n");
# Both the arrays should same number of entries.
my @data = ([20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320],[20,40,80,160,320,640,640,640,640,480,360,120,60,30,10,0]);
my $mygraph = GD::Graph::lines->new(500, 300);
$mygraph->set(
    x_label     => 'Time',
    y_label     => 'Bacterial growth',
    title       => 'Bacterial growth curve') or warn $mygraph->error;
my $myimage = $mygraph->plot(\@data) or die $mygraph->error;
print $myimage->jpeg;
