# Fix problem of high amount of requests
exec {'replace_ulimit':
  command     => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => File['/etc/default/nginx'],
}

file { '/etc/default/nginx':
  ensure => file,
  before => Exec['restart_nginx'],
}

exec {'restart_nginx':
  command     => 'service nginx restart',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Exec['replace_ulimit'],
}
