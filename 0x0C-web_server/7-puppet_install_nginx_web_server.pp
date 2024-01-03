# Setup New Ubuntu server with nginx

exec { 'install_nginx':
  provider => shell,
  command  => 'sudo apt-get -y update' +
              ' && sudo apt-get -y install nginx' +
              ' && echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html' +
              ' && sudo sed -i "/server_name _;/a\ \n\tlocation /redirect_me {\n\t\treturn 301 https://github.com;\n\t}" /etc/nginx/sites-available/default' +
              ' && sudo service nginx start',
}
