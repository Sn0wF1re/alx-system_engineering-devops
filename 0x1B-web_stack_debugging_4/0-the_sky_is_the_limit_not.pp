# Puppet file to configure and fix problem offile opening  limits in nginx

exec {'replacement':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 5000\"/ /etc/default/nginx',
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['replacement'],
}
