#!/usr/bin/php
<?php
$date = date(DATE_RFC2822);
file_put_contents("/home/pi/scripts/deltemp.log", "$date".PHP_EOL, FILE_APPEND);
mysql_connect("localhost", "root", "093833");
file_put_contents("/home/pi/scripts/deltemp.log", "Connect to database OK!".PHP_EOL, FILE_APPEND);
mysql_select_db("home");
mysql_query("DELETE FROM tprocessor ORDER BY time LIMIT 8");
mysql_close();
file_put_contents("/home/pi/scripts/deltemp.log", "Old data deleted!".PHP_EOL, FILE_APPEND);
file_put_contents("/home/pi/scripts/deltemp.log", "__________________________________".PHP_EOL, FILE_APPEND);
?>