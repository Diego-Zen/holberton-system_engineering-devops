# This manifest is to change the ULIMIT for nginx
exec { 'comment-default-ulimit':
  command => "sudo sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\" -n 4096\"/' /etc/default/nginx",
  path    => ['/bin/'],
}
exec { 'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
