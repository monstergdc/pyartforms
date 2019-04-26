<!DOCTYPE HTML>
<html>
<head>
<title>pyartforms (c)2019 Jakub.Noniewicz.art.pl</title>
</head>
<body style="background-color: black; color: white;">
<h2>pyartforms (c)2019 Jakub.Noniewicz.art.pl</h2>
<p>Algorithm-generated art forms in Python.</p>
<p>Click on thumbnail to see bigger image, then refresh to see new variation.</p>
<p>Source code: <a target=_new href="https://github.com/monstergdc/pyartforms">https://github.com/monstergdc/pyartforms</a></p>

<?php
function sub_group($name, $id)
{
	$cnt[1]  = 141;
	$cnt[2]  = 22;
	$cnt[3]  = 78;
	$cnt[4]  = 41;
	$cnt[5]  = 8;
	$cnt[6]  = 18;
	$cnt[7]  = 46;
	$cnt[8]  = 24;
	$cnt[9]  = 64;
	$cnt[10]  = 20;
	$cnt[11]  = 12;
	$cnt[12]  = 16;
	$cnt[13]  = 4;
	$cnt[14]  = 4;
	$cnt[15]  = 55;
	$cnt[16]  = 96;
	$cnt[17]  = 7;
	$cnt[18]  = 6;

	$cnt[101]  = 7; //life
	$cnt[102] = 4; //lissajous
	$cnt[103] = 16; //astro
	$cnt[104] = 2; //mandelbrot
	$cnt[105] = 8; //waves01
	$cnt[106] = 10; //waves02
	$cnt[107] = 1; //waves03

	$cgi = 'pyartw3.py';
	$n = $cnt[$id];
	echo '<tr><td><div style="background-color: #404040; margin-top: 15px; margin-bottom: 15px;">';
	echo '<h2>' . $name . " :: n=(1..." . $n . "):</h2>\n";
	for($i=1;$i<=$n;$i++)
	{
		$pad = '-256x192-' . str_pad($i, 2, '0', STR_PAD_LEFT) . '.png';
		if ($id < 100) $img = 'SMEARS#' . $id . $pad;
		if ($id == 101) $img = 'LIFE' . $pad;
		if ($id == 102) $img = 'LISSAJOUS' . $pad;
		if ($id == 103) $img = 'ASTROART' . $pad;
		if ($id == 104) $img = 'MANDELBROT' . $pad;
		if ($id == 105) $img = 'WAVES#1' . $pad;
		if ($id == 106) $img = 'WAVES#2' . $pad;
		if ($id == 107) $img = 'WAVES#3' . $pad;

		echo '<a target="_blank" href="' . $cgi . '?what=' . $name . '&n=' . $i . '&canvas=800">';
		echo '<img style="width: 256px; float: left; position: absoulte; margin: 2px;" src="minis/' . urlencode($img) . '" title="n='. $i . '">';
		echo "</a>\n";
	}
	echo "</div></td></tr>\n";
}

echo "<table>";
sub_group("mazy01", 1);
sub_group("mazy02", 2);
sub_group("mazy03", 3);
sub_group("mazy04", 4);
sub_group("mazy05", 5);
sub_group("mazy06", 6);
sub_group("mazy07", 7);
sub_group("mazy08", 8);
sub_group("mazy09", 9);
sub_group("mazy10", 10);
sub_group("mazy11", 11);
sub_group("mazy12", 12);
sub_group("mazy13", 13);
sub_group("mazy14", 14);
sub_group("mazy15", 15);
sub_group("mazy16", 16);
sub_group("mazy17", 17);
sub_group("mazy18", 18);
sub_group("life", 101);
sub_group("lissajous", 102);
sub_group("astro", 103);
sub_group("mandelbrot", 104);
sub_group("waves01", 105);
sub_group("waves02", 106);
sub_group("waves03", 107);
echo "</table>";
?>

</body>
</html>
