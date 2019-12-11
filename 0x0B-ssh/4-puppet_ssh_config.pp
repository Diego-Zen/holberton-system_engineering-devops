# change client configuration file to connect a server without typing a password
file { 'ssh-config':
  ensure => present
  path   => '/etc/ssh/ssh_config',
}

file_line { 'pass':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication yes',
  match => '^PasswordAuthentication*'
}

file_line { 'id':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}
