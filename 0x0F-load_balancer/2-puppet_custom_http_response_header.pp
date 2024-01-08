# Update the package list
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

# Install Nginx
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

# Add custom HTTP header to Nginx configuration
exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],  # Set the HOST environment variable
  command     => 'sudo sed -i '\''s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By "$HOST";/'\'' /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

# Restart Nginx service
exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
