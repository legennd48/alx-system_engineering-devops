# kill a progem call killmenow

exec {'killmenow':
  command => '/usr/bin/pkill -f "killmenow"',
  onlyif  => '/usr/bin/pgrep -f "killmenow"'
  }
