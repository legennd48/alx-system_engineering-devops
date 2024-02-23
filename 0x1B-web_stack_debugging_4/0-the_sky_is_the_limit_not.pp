# modify config to increase limit
# increase limit

exec { 'Fix_-imit':
  command => '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx',
}
