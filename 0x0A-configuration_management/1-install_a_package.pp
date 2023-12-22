# Using Puppet to install Flask and its dependencies from pip3

# Install Python 3
package { 'python3':
  ensure => present,
}

# Install Python 3 pip
package { 'python3-pip':
  ensure => present,
}

# Install Flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
