# puppet manifest for creating a file in /tmp
file { 'create a file':
    path    => '/tmp/holberton',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
