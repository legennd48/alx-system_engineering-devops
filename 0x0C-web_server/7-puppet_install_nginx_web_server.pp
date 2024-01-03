# Setup New Ubuntu server with nginx

# execue update command
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# install nginx
package { 'nginx':
  ensure => 'installed',
}

# Create index
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# configure redirect 301
exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://github.com" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
