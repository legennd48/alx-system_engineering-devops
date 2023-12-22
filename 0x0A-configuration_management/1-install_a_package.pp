# Using Puppet to install a Python package (Flask)
package { 'flask':
  ensure   => '2.1.0',   # Ensure package version
  provider => 'pip3',    # Sets package provider
}
