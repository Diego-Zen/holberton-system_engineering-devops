# puppet manifest for killing a proces call killmenow
exec { 'process-kill'
    command => 'pkill killmenow'
}
