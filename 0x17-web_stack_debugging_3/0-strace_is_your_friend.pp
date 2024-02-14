# puppet to automate fixing errors in server

exec { 'fix typo':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
