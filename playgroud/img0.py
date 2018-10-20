#!/usr/bin/env python


#example of CGI sending static image


import sys, os

src =  "tmp.png"

sys.stdout.write("Content-Type: image/png\n")
sys.stdout.write("Content-Length: " + str(os.stat(src).st_size) + "\n")
sys.stdout.write("\n")
sys.stdout.flush()
sys.stdout.buffer.write(open(src, "rb").read())
