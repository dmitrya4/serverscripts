#!/usr/bin/php
<?php

$filename = "/sys/class/thermal/thermal_zone0/temp";
$handle = fopen($filename, "r");
$content = fread($handle, filesize($filename));
$result = intval($content/1000);
echo $result;
file_put_contents("/home/pi/scripts/tproc.log", "$result".PHP_EOL, FILE_APPEND);
fclose($handle);

$link = mysql_connect('localhost', 'root', '093833') or die ("Could not connect:" .mysql_error());
file_put_contents("/home/pi/scripts/tproc.log", "$link".PHP_EOL, FILE_APPEND);
mysql_select_db('home') or die ("Could not select database");
mysql_query("INSERT INTO tprocessor(time, t) VALUES(NOW(), $result)");
mysql_close($link);
file_put_contents("/home/pi/scripts/tproc.log", "Finished".PHP_EOL, FILE_APPEND);
?>