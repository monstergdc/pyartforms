<!DOCTYPE HTML>
<html>
<head>
<title>pyartforms (c)2019 Noniewicz.art.pl</title>
</head>
<body style="background-color: black; color: white;">

<?php
function sub_group($name, $id)
{
	$cnt[1]  = 13;	//smears
	$cnt[2]  = 9;
	$cnt[3]  = 54;
	$cnt[4]  = 26;
	$cnt[5]  = 6;
	$cnt[6]  = 9;
	$cnt[7]  = 34;
	$cnt[8]  = 4;
	$cnt[9]  = 58;
	$cnt[10]  = 20;
	$cnt[11]  = 3;
	$cnt[12]  = 16;
	$cnt[13]  = 4;
	$cnt[14]  = 4;
	$cnt[15]  = 336;
	$cnt[16]  = 144;

//	$cnt[101]  = 7; //life
//	$cnt[102] = 3; //lissajous
	$cnt[103] = 16; //astro
//	$cnt[104] = 9; //waves
//	$cnt[105] = 2; //mandelbrot

	$cgi = 'pyartw3.py';
	$n = $cnt[$id];
	echo '<tr><td><div style="background-color: #404040; margin-top: 15px; margin-bottom: 15px;">';
	echo '<h2>' . $name . " :: n=(1..." . $n . "):</h2>\n";
	for($i=1;$i<=$n;$i++)
	{
		if ($id < 100) $img = 'minis/SMEARS%23' . $id . '-256x192-' . str_pad($i, 2, '0', STR_PAD_LEFT) . '.png';
		if ($id == 103) $img = 'minis/astro' . '-256x192-' . str_pad($i, 3, '0', STR_PAD_LEFT) . '.png';

		echo '<a target="_blank" href="' . $cgi . '?what=' . $name . '&n=' . $i . '&canvas=800">';
		echo '<img style="width: 256px; float: left; position: absoulte; margin: 2px;" src="' . $img . '" title="n='. $i . '">';
		echo "</a>\n";
	}
	echo "</div></td></tr>\n";
}

echo "<table>";
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
sub_group("smears12", 12);
sub_group("smears13", 13);
sub_group("smears14", 14);
sub_group("smears15", 15);
sub_group("smears16", 16);
//---
//sub_group("life", 101);
//sub_group("lissajous", 102);
sub_group("astro", 103);
//sub_group("waves", 104);
//sub_group("mandelbrot", 105);
echo "</table>";
?>

</body>
</html>
