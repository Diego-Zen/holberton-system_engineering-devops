# This manifest is to change the ULIMIT for nginx
exec { 'comment-default-ulimit':
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\" -n 4096\"/g' /etc/default/nginx",
  path    => ['/bin/'],
}
exec { 'restart-nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}
