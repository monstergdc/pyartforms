<!DOCTYPE HTML>
<html>
<head>
<title>pyartforms (c)2019 Noniewicz.art.pl</title>
</head>
<body style="background-color: black; color: white;">

<?php
function sub_group($name, $id)
{
	$cnt[1]  = 13;
	$cnt[2]  = 4;
	$cnt[3]  = 54;
	$cnt[4]  = 26;
	$cnt[5]  = 5;
	$cnt[6]  = 5;
	$cnt[7]  = 34;
	$cnt[8]  = 4;
	$cnt[9]  = 58;
	$cnt[10]  = 20;
	$cnt[11]  = 3;

	$cnt[101]  = 7; //life
	$cnt[102] = 3; //lissajous
	$cnt[103] = 16; //astro
	$cnt[104] = 9; //waves
	$cnt[105] = 2; //mandelbrot

	$cgi = 'pyartw3.py';
	$n = $cnt[$id];
	echo "<h2>" . $name . " :: n=&nbsp;\n";
	for($i=1;$i<=$n;$i++)
	{
		echo '<a target="_blank" href="' . $cgi . '?what=' . $name . '&n=' . $i . '&canvas=800">' .$i . '</a>&nbsp;' . "\n";
	}
	echo "\n</h2>\n<hr>\n";
}

sub_group("smears1", 1);
sub_group("smears2", 2);
sub_group("smears3", 3);
sub_group("smears4", 4);
sub_group("smears5", 5);
sub_group("smears6", 6);
sub_group("smears7", 7);
sub_group("smears8", 8);
sub_group("smears9", 9);
sub_group("smears10", 10);
sub_group("smears11", 11);

sub_group("life", 101);
sub_group("lissajous", 102);
sub_group("astro", 103);
sub_group("waves", 104);
sub_group("mandelbrot", 105);
?>

</body>
</html>
