# Fix bad extension is settings file
exec {
    command => "sed -i 's/phpp/php/g' /var/html/wp-settings.php"
}
