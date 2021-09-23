#!/usr/bin/env perl

use strict;
use warnings;

sub main() {
  print "Content-Type:text/plain\r\n\r\n";  
  my $data = <STDIN>;
  chomp $data;
  my ($page, $params) = split / /, $data, 2;
  if ($page % 10 != 0) {
    prnfile($page, $params);
  } else {
    my @params2 = split / /, $params, 2;
    excfile($page, $params2[0], @params2 > 1 ? $params2[1] : '');
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
  my @files = glob "dat/$pg.*";
  if (@files < 1) {
    print "No checker $pg\n";
    return;
  }
  my $f = $files[0];
  my $res = '';
  if ($f =~ /.*\.sh/) {
    $res = `bash $f $hs '$ans'`;
  } elsif ($f =~ /.*\.py/) {
    $res = `python3 $f $hs '$ans'`;
  } elsif ($f =~ /.*\.pl/) {
    $res = `perl $f $hs '$ans'`;
  } else {
    print "Unknown checker type $pg\n";
    return;
  }
  if ($? != 0) {
    print "Checker failed\n";
  } else {
    print $res;
  }
}

main();


