# pyartforms

My playground for tests in computer-generated art forms (graphics, video, sound). 
Stuff here may change, may be incomplete or not fully working, may be w/o docs, etc. 
as it is work and experiments in progress. Also no error checking. Tested only under Windows (paths!).

Feel free to tinker with it.

Many scripts will generate multiple images for different presets, most will be in A3 print-ready format.

Prerequisites include:

pip install pillow
and
pip install opencv-python
for video

# LIFE:
script: life1.py

![example](/examples/life-0001.png?raw=true "Life example")
![example](/examples/life-0003.png?raw=true "Life example")
![example](/examples/life-0005.png?raw=true "Life example")
![example](/examples/life-0007.png?raw=true "Life example")

# LISSAJOUS:
script: lissajous.py

![example](/examples/liss-0003.png?raw=true "Lissajous example")

# ASTROFORMS:
script: astroart.py

![example - neutron star](/examples/zz-04-neutronstar-cir.png?raw=true "Astro example - neutron star")

# SMEARS:
script: smears1234.py

![example - mazy1](/examples/mazy1-4960x3507-01-003.png?raw=true "Smears#1 example")
![example - mazy1](/examples/mazy1-4960x3507-02-003.png?raw=true "Smears#1 example")
![example - mazy1](/examples/mazy1-4960x3507-06-002.png?raw=true "Smears#1 example")
![example - mazy2](/examples/mazy2-4960x3507-05-004.png?raw=true "Smears#2 example")
![example - mazy4](/examples/mazy4-4960x3507-01-002.png?raw=true "Smears#4 example")
![example - mazy4](/examples/mazy4-4960x3507-05-003.png?raw=true "Smears#4 example")
![example - mazy4](/examples/mazy4-4960x3507-07-003.png?raw=true "Smears#4 example")

# GROWING PLANTS:
script: grow.py

[Growing plants video example#1](https://www.youtube.com/watch?v=5HrdduqAdVk)

![example#1](/examples/tree0.png?raw=true "Tree example #1")

# MANDELBROT FRACTAL:
script: mandelbrot.py

![example](/examples/mandel-002.png?raw=true "Mandelbrot example")

# ASCII ART:
script: asciiart.py

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
