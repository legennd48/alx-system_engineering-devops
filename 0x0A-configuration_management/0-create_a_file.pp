# creating a file in /tmp with owner, group, permission and content configured

file {'/tmp/school':
  ensure  => file, # ensure it is a file if it is already present
  content => 'I love Puppet', # sets the content of the file
  owner   => 'www-data', # Sets the owner of the file
  group   => 'www-data', # Sets the group of hte filr
  mode    => '0744', # Sets file permission
  }
