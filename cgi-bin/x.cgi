#!/usr/bin/env perl

use strict;
use warnings;

sub main() {
  print "Content-Type:text/plain\r\n\r\n";  
  my $data = <STDIN>;
  chomp $data;
  my ($pg, $p1, $p2) = split / /, $data;
  if ($pg % 10 != 0) {
    prnfile($pg, $p1);
  } else {
    excfile($pg, $p1, $p2);
  }
}

sub prnfile() {
  my ($pg, $flags) = @_;
  my $f;
  if (!open($f, '<', "dat/$pg.txt")) {
    print "Ah, zaichiki!\n";
    return;
  }
  my %flags = ();
  foreach my $ff (split /\,/, $flags) {
    $flags{$ff} = 1;
  }
  while (my $line = <$f>) {
    if (substr($line, 0, 1) eq '?') {
      my $p = 1;
      if (substr($line, 1, 1) eq '!') {
        $p += 1;
      }
      my ($key, undef) = split / /, substr($line, $p), 2;
      if ((exists $flags{$key}) ne ($p == 1)) {
        next;
      }
      $line = substr($line, $p + length($key) + 1);
    }
    print $line;
  }
  close($f);
}

sub excfile() {
  my ($pg, $hs, $ans) = @_;
  my $res = `bash dat/$pg.sh $hs $ans`;
  if ($? != 0) {
    print "Aw, medvediki!\n";
  } else {
    print $res;
  }
}

main();


