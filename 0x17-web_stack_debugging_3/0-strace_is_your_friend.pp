# Fix bad extension in settings file
exec { 'fix-config':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path => ['/bin']
}
