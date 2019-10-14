use Net::Ping;
use Proc::Background;

my $p = Net::Ping->new("icmp");

if ($p->ping("8.8.8.8")){
  unlink '/tmp/error';
  my $pb = Proc::Background->new("/usr/bin/python /home/pi/pi/clock.py");
  $pb->wait();
} else {
  if (-e '/tmp/error'){

  } else {
    my $pb = Proc::Background->new("/usr/bin/python /home/pi/pi/down.py");
    $pb->wait();
    my $pb2 = Proc::Background->new("/usr/bin/touch /tmp/error");
    $pb2->wait();
  }
}
