# using puppet to install a package

package {'flask':
  ensure   => '2.1.0', # ensure package version
  provider => 'pip3', # sets package provider
  }
