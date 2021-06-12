# pyartforms

## Generative art in Python

My playground for tests in computer-generated art forms (graphics, video, sound). 
Many scripts will generate multiple images for different presets, most will be in A3 print-ready format (available formats include A7..A0 and 2A0, 4A0, also some B-formats are defined).
Feel free to tinker with it. Get inspired.

Stuff here may change, may be incomplete or not fully working, may be w/o docs, etc. 
as it is work and experiments in progress. Also no error checking. Tested only under Windows (paths!).

- Small demo in: **pyart-demo.py** (possibly not everything yet). 
- Web/CGI version in: **pyartw3.py** (also possibly not all yet). 
- GUI version in: **pyart-wxGUI.py** (just started).

Actual definitions reside in file: *pyart_defs.py*.

Prerequisites include: **pip install pillow** and for video: **pip install opencv-python**, 
possibly also **pip install cgi** for CGI version 
and **pip install -U wxPython** for GUI version.



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

![example - mazy1](/examples/SMEARS1-1748x1240-04-001-20190422132718.png?raw=true "Smears#1 example")
![example - mazy1](/examples/SMEARS1-1748x1240-23-001-20190422132718.png?raw=true "Smears#1 example")
![example - mazy1](/examples/SMEARS1-1748x1240-26-001-20190422132718.png?raw=true "Smears#1 example")
![example - mazy1](/examples/SMEARS1-1748x1240-27-001-20190422132718.png?raw=true "Smears#1 example")
![example - mazy1](/examples/SMEARS1-1748x1240-43-001-20190422132718.png?raw=true "Smears#1 example")
![example - mazy1](/examples/SMEARS1-1748x1240-46-001-20190422132718.png?raw=true "Smears#1 example")
![example - mazy2](/examples/SMEARS2-1748x1240-15-001-20190422133254.png?raw=true "Smears#2 example")
![example - mazy4](/examples/SMEARS4-1748x1240-01-001-20190422133419.png?raw=true "Smears#4 example")
![example - mazy4](/examples/SMEARS4-1748x1240-06-001-20190422133419.png?raw=true "Smears#4 example")
![example - mazy4](/examples/SMEARS4-1748x1240-37-001-20190422133419.png?raw=true "Smears#4 example")
![example - mazy6](/examples/SMEARS6-1748x1240-05-001-20190422133450.png?raw=true "Smears#6 example")
![example - mazy6](/examples/SMEARS6-1748x1240-09-001-20190422133450.png?raw=true "Smears#6 example")
![example - mazy7](/examples/SMEARS7-1748x1240-25-001-20190422133459.png?raw=true "Smears#7 example")
![example - mazy9](/examples/SMEARS9-1748x1240-33-001-20190422133516.png?raw=true "Smears#9 example")
![example - waves1](/examples/WAVES1-1748x1240-01-001-20190422130753.png?raw=true "Smears#25 example")
![example - waves1](/examples/WAVES1-4960x3507-02-001-20190422130757.png?raw=true "Smears#25 example")

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

# REPIXELIZE:
script: **repixelize.py** and **repixelize-demo.py**

eg. this 256x192 small image
![small source image](/playgroud/repixel-in/zz-zx-0011-1-cir.png?raw=true "small source image")
can be remade into bigger (800x600 here) image with different 'finish' style:
![example](/examples/repixel-demo.png?raw=true "Repixelize example")
