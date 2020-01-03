# change client configuration file to connect a server without typing a password
file { 'ssh-config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
}
# set password auth to no
file_line { 'pass':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication*',
}
# add identity for holberton key if not exist
file_line { 'id':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
