# pyartforms

## Generative art in Python

My playground for tests in computer-generated art forms (graphics, video, sound). 
Many scripts will generate multiple images for different presets, most will be in A3 print-ready format (available formats include A7..A0 and 2A0, 4A0, also some B-formats are defined).
Feel free to tinker with it. Get inspired.

Stuff here may change, may be incomplete or not fully working, may be w/o docs, etc. 
as it is work and experiments in progress. Also no error checking. Tested only under Windows (paths!).

Small demo is in: **pyart-demo.py** (possibly not everything yet).
Web/CGI version in: **pyartw3.py** (also possibly not all yet).
GUI version in: **pyart-wxGUI.py** (just started).

Actual definitions reside in file: *pyart_defs.py*.

Prerequisites include: **pip install pillow** and for video: **pip install opencv-python**, possibly also **pip install cgi**



# SOME GIF-LIKE ANIMATIONS:
script: **anims.py** and **zxoids-anim.py**

[anim 01 video](https://www.youtube.com/watch?v=-vyr4g9q0Go)
[anim 02 video](https://www.youtube.com/watch?v=3LewUnBFg2c)
[anim 04 video](https://www.youtube.com/watch?v=SGWo8JxQPTU)

# LIFE:
script: **life1.py**

![example](/examples/life-0003.png?raw=true "Life example")
![example](/examples/life-0007.png?raw=true "Life example")

# LIFE 2D - IMAGES+ANIMATIONS (alive image eaters):
script: **life2.py**

[Life2d video example#1](https://www.youtube.com/watch?v=FofqSbcO2W8)
[Life2d video example#2](https://www.youtube.com/watch?v=Ce1yVJNs3AM)

![example](/examples/zz-life2d-001-f2a.png?raw=true "Life example")
![example](/examples/zz-life2d-001-f2b.png?raw=true "Life example")

# ASTROFORMS:
script: **astroart.py**

![example - neutron star](/examples/zz-04-neutronstar-cir.png?raw=true "Astro example - neutron star")
![example - supernova](/examples/zz-astro-06-supernova-cir.png?raw=true "Astro example - supernova")

# SMEARS:
script: **smears.py**

![example - mazy1](/examples/mazy1-4960x3507-01-003.png?raw=true "Smears#1 example")
![example - mazy1](/examples/mazy1-4960x3507-02-003.png?raw=true "Smears#1 example")
![example - mazy1](/examples/mazy1-4960x3507-06-002.png?raw=true "Smears#1 example")
![example - mazy4](/examples/mazy4-4960x3507-01-002.png?raw=true "Smears#4 example")
![example - mazy4](/examples/mazy4-4960x3507-05-003.png?raw=true "Smears#4 example")
![example - mazy4](/examples/mazy4-4960x3507-07-003.png?raw=true "Smears#4 example")

# WAVES:
script: **waves.py**

![example - waves1](/examples/waves1-4960x3507-03-003.png?raw=true "Waves#1 example")
![example - waves3](/examples/waves3-4960x3507-01-003.png?raw=true "Waves#3 example")

# LISSAJOUS:
script: **lissajous.py**

![example](/examples/liss-0003.png?raw=true "Lissajous example")

# CITY (LAME):
script: **city-lame.py**

![example - city1](/examples/city1-4960x3507-01-001.png?raw=true "City#1 example")

# GROWING PLANTS:
script: **grow.py**

[Growing plants video example#1](https://www.youtube.com/watch?v=5HrdduqAdVk)

![example#1](/examples/tree0.png?raw=true "Tree example #1")

# MANDELBROT FRACTAL:
script: **mandelbrot.py**

![example](/examples/mandel-002.png?raw=true "Mandelbrot example")

# ASCII ART:
script: **asciiart.py**

<pre>
++++++*************:::::::::::::::::#WW@@@@#:..........................,,,,,,,...........
++++++************+::::::::::::::::#WWW@@@@@@+....................,.,,,,,,,,.............
++++++************:::::::::::::::::@WWWWW@@@@W*..................,,,,..,..,,,,...........
++++++***********+:::::::::::::::::@WWWW@@@WW@@:.................,,,,,,,,,,,,,,..........
++++++***********::::::::::::::::::*WWWW@@@@@@@+..:...............,,,,,,,,,,,,...........
++++++**********+:::::::::::::::::::@WWW@@@@@@@WWW@WW@@@@@@#+.....::+:+*#@@@*::++........
++++++**********::::::::::::::::::::@WWWWW@@@@@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*.....
+++::**********+:::::::::::::::::::*WWWWWWW@@@WWWWWWWWWWWWWWWWWWWWWWWWWWWW*:**#@WWWW*....
:::::**********:::::::::::::::#@@@@WWWWWWWWW@@WWWWWWWWWWWWWWWWWWWWWW@+.,.........+:......
::::+*********+:::::::::::::#WWWWWWWWWWWWWWWW@@WWW+..........,,,.,,,.....................
::::+*********:::::::::::::+WWWWWWWWWWWWWWWWW@@@W#.........,,,,,,,.......................
::::+********+::::::::::::+WWWWWWWWWWWWWWWWWW@@@W*........,,,,,.,........................
::::+********::::::::::::+@WWWWWWWWWWWWWWWWWW@@WW..:.......,,,...........................
::::+*******+:::::::::::@WWWWWWWWWWWWWWWWWWWWWWW@#***+.....,.............................
::::********+:::::::::*WWWWWWWWWWWWWWWWWWWWWWWW@###***+..................................
::::*******:::::::::+@WWWWWW@:WWWWWWWWWWWWWWWWW*###****...................::++:..........
:::+******+::::::+@WWWWWWWW+::#WWWWWWWWWWWWWWW#:####**+............:+***********+........
:::+*****+::::@WWWWWWWWW@:::::+WWWWWWWWWWWWWWW:.*####*.......:+*********.....:+..........
:::+*****+::@WWWWWWWW@+::::::.:WWWWWWWWWWWWWW@..+##**..+************+....................
:::+****+::@WWWW+++:::::::::...@WWWWWWWWWWWWW@..*#******#####**+.........................
:::+****+:@WWWW#++::::::::::..:WWWWWWWWWWWWWWW###********#:.............................:
:::****+:*WWW@#:+:::::::::::.:@WWWWWWWWWWWWWWW@##*******#...............................:
::+****:::@@#*:::::::::::::::@WWWWWWWWWWWWWWWWW#######*#*...........................:::::
::+***+:::::::::::::::::::+@WWWWWWWWWWWWWWWWWWW@########:.............................:::
::+***+::::::::::::::::::#WWWWWWWWWWWWWWWWWWWWW@#######*..............................:::
::+**+::::::::::::::::::#WWWWWWWWWWWWWWWWWWWWWWW@######:.............................::::
::+**::::::::::::::::::#WWWWWWWWWWWWWWWWWWWWWWWW@#####*.............................:.:::
::**+:::::::::::::::::#WWWWWWWWWWWWWWWWWWWWWWWWW@##*##+.............................:::::
::**+::::::::::::::::#WWWWWWWWWWWWWWWWWWWWWWWWWW@##*##:........:...................::::::
:+*+::::::::::::::::*WWWWWWWWWWWWWWWWWWWWWWWWWWW#****#:........::::::.........:::.:::::::
:+*+::::::::::::::@WWWWWWWWWWWW@+:+WWWWWWWWWWWW@*******......:::::::::........:::::::::::
:++:::::::::::::*WWW@WWWWWWW#...:::.@WWWWWWWWWW@##****+......:::::::::......:::::::::::::
:+:::::::::::::*WWWWWWWWWW+......::+@WWWWWWWWWW####**#*....:::::::::::.......::::::::::::
:+::::::::::::#WWWWWWW*......*###**@WWWWWWWWWW@#######+.....::::::::::.....::::::::::::::
:::::::::::::@WWWWW@*......+#######WWWWWWWWWWW@#######.........::::::::......::::::::::::
:::::::#@@@WWWWW+.......:#########@WWWWWWWWWW*.######+...........::::::...:::::::::::::::
:::::#@WWWWWWWW#+##@##@#####*:...:WWWWWWWWWWW.######*.............::::::...::::::::::::::
:::::WWWW@*:::.#@@@@@@@#:........+WWWWWWWWWW*+######:.............:::::::..::::::::::::::
:::::*+::::::::@@@*:.............*WWWWWWWWW@.######*..............:::::::.:::::::::::::::
:::::::::::::::..................@WWWWWWWWW+.######.................:::::::::::::::::::::
:::::::::::::::.................:WWWWWWWWW#.*#####:.............:::::::::::::::::::::::::
:::::::::::::::.................*WWWWWWWW@..#####+...............::::::::..::::::::::::::
</pre>
