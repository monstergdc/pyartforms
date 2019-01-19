﻿<html>
<head>
<title>pyartforms (c)2019 Noniewicz.art.pl</title>
</head>
<body style="background-color: black; color: white;">

<?php
function sub_group($name, $id)
{
	$cnt[1]  = 11;
	$cnt[2]  = 5;
	$cnt[3]  = -1;	//7
	$cnt[4]  = 9;
	$cnt[5]  = 5;
	$cnt[6]  = 5;
	$cnt[7]  = 22;
	$cnt[8]  = 3;
	$cnt[9]  = 7; //life
	$cnt[10] = 3; //lissajous
	$cnt[11] = 16; //astro
	$cnt[12] = 9; //waves
	$cnt[13] = 2; //mandelbrot

	$cgi = 'pyartw3.py';
	$n = $cnt[$id];
	echo "<h2>" . $name . "</h2>\n";
	for($i=1;$i<=$n;$i++)
	{
		echo '<img src="' . $cgi . '?what=' . $name . '&n=' . $i . '&canvas=256">&nbsp;';
	}
	echo "\n<hr>\n";
}

sub_group("smears1", 1);
sub_group("smears2", 2);
//3?
sub_group("smears4", 4);
sub_group("smears5", 5);
sub_group("smears6", 6);
sub_group("smears7", 7);	//fix
sub_group("smears8", 8);
sub_group("life", 9);
sub_group("lissajous", 10);
sub_group("astro", 11);
sub_group("waves", 12);	//fix
sub_group("mandelbrot", 13);
?>

</body>
</html>