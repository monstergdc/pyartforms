
# Python art forms
# some common code/tools
# (c)2018 Noniewicz.com
# upd: 20180503, 08
# upd: 20181020

from PIL import Image, ImageDraw, ImageFilter
from datetime import datetime as dt
from array import array
import numpy as np
import cgi


# https://en.wikipedia.org/wiki/Paper_size

CANVASES = {
    'A5': (2480, 1748),
    'A4': (3507, 2480),	 # rule is: 29.7/2.54*300 x 21/2.54*300
    'A3': (4960, 3507),
    'A2': (7015, 4960),
    'A1': (9933, 7015),
    'A0': (14043, 9933),
    'B0': (16700, 11811),
    '256': (256, 192),
    '512': (256*2, 192*2),
    '640': (640, 480),
    '720': (720, 576),
    '800': (800, 600),
    '1024' : (1024, 768),
    '2000' : (2000, 1500),
    '4000' : (4000, 3000),
    '8000' : (8000, 6000)
}

def get_canvas(name):
    return CANVASES.get(name, (0,0))

def get_canvas(name):
    wh = CANVASES.get(name, (0,0))
    return wh[0], wh[1]

def circle(draw, x, y, r, fill, outline):
    xy = [(x-r, y-r), (x+r, y+r)]
    draw.ellipse(xy, fill=fill, outline=outline)

def box(draw, x, y, r, fill, outline):
    xy = [(x-r, y-r), (x+r, y+r)]
    draw.rectangle(xy, fill=fill, outline=outline)

def triangle(draw, points, fill, outline):
    draw.polygon(points, fill=fill, outline=outline)

def gradient(FColorStart, FColorMid, FColorEnd, i, n):
    n2 = n/2
    downc = (n2-i)/n2
    upc = i/n2
    r1 = int( FColorStart[0]*downc + FColorMid[0]*upc )
    g1 = int( FColorStart[1]*downc + FColorMid[1]*upc )
    b1 = int( FColorStart[2]*downc + FColorMid[2]*upc )
    downc = (n2-i/2)/n2
    upc = i/2/n2
    r2 = int( FColorMid[0]*downc + FColorEnd[0]*upc )
    g2 = int( FColorMid[1]*downc + FColorEnd[1]*upc )
    b2 = int( FColorMid[2]*downc + FColorEnd[2]*upc )
    if i < n/2:
        return (r1, g1, b1)
    else:
        return (r2, g2, b2)

def gradient2(FColorStart, FColorEnd, i, n):
    downc = ((n)-i)/(n)
    upc = i/(n)
    r1 = int( FColorStart[0]*downc + FColorEnd[0]*upc )
    g1 = int( FColorStart[1]*downc + FColorEnd[1]*upc )
    b1 = int( FColorStart[2]*downc + FColorEnd[2]*upc )
    return (r1, g1, b1)

def script_it(draw, xy, font, size, fill):
    fnt = ImageFont.truetype(font, size)
    draw.text(xy, "Noniewicz.art.pl", font=fnt, fill=fill)

def im2cgi(im, format='PNG'):
    ct = ''
    if format == 'PNG':
        ct = 'image/png'
    if format == 'JPG':
        ct = 'image/jpg'
    if format == 'GIF':
        ct = 'image/gif'
    if ct == '':
        ct = 'image/png'
        format='PNG'
    imgByteArr = io.BytesIO()
    im.save(imgByteArr, format=format)
    imgByteArr = imgByteArr.getvalue()
    sys.stdout.write("Content-Type: "+ct+"\n")
#todo: fin
#    sys.stdout.write("Content-Length: " + str(?) + "\n")
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write(imgByteArr)
    sys.stdout.flush()

def art_painter(params, png_file='example.png', output_mode='save'):
    if output_mode == 'save':
        start_time = dt.now()
        print('drawing %s... %s' % (params['name'], png_file))
    im = Image.new('RGB', (params['w'], params['h']), params['Background'])
    draw = ImageDraw.Draw(im)
    f = params['call']
    f(draw, params)
    xsmooth(params, im)
    if output_mode == 'save':
        im.save(png_file, dpi=(300,300))
        show_benchmark(start_time)
    else:
        im2cgi(im, format='PNG')

def get_cgi_par(default=None):
    form = cgi.FieldStorage()
    if default == None:
        par = {'w': 800, 'h': 600, 'f': ''}
    else:
        par = default
    if "w" in form:
        par['w'] = int(form["w"].value)
    if "h" in form:
        par['h'] = int(form["h"].value)
    if "f" in form:
        par['f'] = form["f"].value
    return par

def show_benchmark(start_time):
    time_elapsed = dt.now() - start_time
    print('done. elapsed time: {}'.format(time_elapsed))
    return time_elapsed

# image to array
def im2arr(image_path):
    #im = Image.load(image_path)
    im = Image.open(image_path)
    im = im.convert('L')
    a = np.fromiter(iter(im.getdata()), np.uint8) # BW?
    a.resize(im.height, im.width)
    return a

def xsmooth(params, im):
    if not "blur" in params:
        return
    if params['blur'] == True:
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.BLUR)
        im = im.filter(ImageFilter.SHARPEN)
        im = im.filter(ImageFilter.SHARPEN)
