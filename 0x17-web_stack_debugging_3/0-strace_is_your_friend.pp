# Changes extensions from .phpp to .php in the WordPress file wp-settings.php.

exec { 'fixWP':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
