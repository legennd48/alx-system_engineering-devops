# kill a process called killmenow

exec {'killmenow':
  command => '/usr/bin/pkill -f "killmenow"',
  onlyif  => '/usr/bin/pgrep -f "killmenow"'
  }
