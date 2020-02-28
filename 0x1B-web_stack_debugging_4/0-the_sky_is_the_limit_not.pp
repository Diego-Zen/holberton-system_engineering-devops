# This manifest is to change the ULIMIT for nginx
exec { 'comment-default-ulimit':
  command => "sed '/ULIMIT=\"-n 15\"/ s/^/#/' /etc/default/nginx",
  path    => ['/bin/'],
}
exec { 'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
