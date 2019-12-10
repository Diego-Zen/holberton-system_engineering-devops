# puppet manifest for killing a process called killmenow
exec { 'process-kill'
  command => 'pkill killmenow',
  provider => 'shell'
}
