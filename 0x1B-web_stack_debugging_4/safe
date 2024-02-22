# increase request limit at nginx

exec { 'fix nginx':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell
}

# Restart Nginx
-> exec { 'restart nginx':
  command  => 'sudo nginx restart',
  provider => bash
}
