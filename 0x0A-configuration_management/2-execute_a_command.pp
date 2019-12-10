# puppet manifest for killing a process called killmenow
exec { 'process-kill'
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell'
}
