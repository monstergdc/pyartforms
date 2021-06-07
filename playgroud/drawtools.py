
# PyArtForms - Python generative art forms paint algorithms (artificial artist)
# some common code/tools
# (c)2018-2021 Noniewicz.com
# upd: 20180503, 08
# upd: 20181020, 21
# upd: 20190112, 19, 21, 22
# upd: 20190311, 29
# upd: 20190414, 21
# upd: 20210301
# upd: 20210507, 15, 23, 26, 27
# upd: 20210606, 07

from PIL import Image, ImageDraw, ImageFilter, PngImagePlugin, ImageFont, ImageOps
from datetime import datetime as dt
import random, math, string, os, sys, io
from array import array
import numpy as np
import cgi


# https://en.wikipedia.org/wiki/Paper_size

CANVASES = {
    'A7': (1240, 874),
    'A6': (1748, 1240), # note: almost like 10x15 cm photo
    'A5': (2480, 1748),
    'A4': (3507, 2480),	# note: for cm rule is: 29.7/2.54*300 x 21/2.54*300 (in*DPI=300)
    'A3': (4960, 3507),
    'A2': (7015, 4960),
    'A1': (9933, 7015),
    'A0': (14043, 9933),
    '4A0': (28086, 19866),
    '2A0': (19866, 14043),

    'B7': (1476, 1039),
    'B6': (2078, 1476),
    'B5': (2952, 2078),
    'B4': (4169, 2952),
    'B3': (5905, 4169),
    'B2': (8350, 5905),
    'B1': (11811, 8350),
    'B0': (16700, 11811),

    '128': (128, 96),
    '256': (256, 192),
    '320': (320, 200),
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

def rect(draw, x, y, w, h, fill, outline):
    xy = [(int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2))]
    draw.rectangle(xy, fill=fill, outline=outline)

def triangle(draw, points, fill, outline):
    draw.polygon(points, fill=fill, outline=outline)

def gradient(colorStart, colorMid, colorEnd, i, n):
    """Return gradient color i of n in colorStart..colorMid..colorEnd range."""
    # note: weird, py 2.7 needs these float conversions, on 3.6 it was ok
    n2 = float(n/2)
    if i < n/2:
        downc = float(n2-i)/n2
        upc = float(i)/n2
        r1 = int( float(colorStart[0])*downc + float(colorMid[0])*upc )
        g1 = int( float(colorStart[1])*downc + float(colorMid[1])*upc )
        b1 = int( float(colorStart[2])*downc + float(colorMid[2])*upc )
        return (r1, g1, b1)
    else:
        i2 = float(i - n2)
        downc = float(n2-i2)/n2
        upc = float(i2)/n2
        r2 = int( float(colorMid[0])*downc + float(colorEnd[0])*upc )
        g2 = int( float(colorMid[1])*downc + float(colorEnd[1])*upc )
        b2 = int( float(colorMid[2])*downc + float(colorEnd[2])*upc )
        return (r2, g2, b2)

def gradient2(colorStart, colorEnd, i, n):
    """Return gradient color i of n in colorStart..colorEnd range."""
    downc = float(n-i)/float(n)
    upc = float(i)/float(n)
    r1 = int( float(colorStart[0])*downc + float(colorEnd[0])*upc )
    g1 = int( float(colorStart[1])*downc + float(colorEnd[1])*upc )
    b1 = int( float(colorStart[2])*downc + float(colorEnd[2])*upc )
    return (r1, g1, b1)

def script_it(draw, xy, font, size, fill):
    fnt = ImageFont.truetype(font, size)
    draw.text(xy, "Jakub.Noniewicz.art.pl", font=fnt, fill=fill)

def add_myself(draw, w, h, bg):
    """Mark image authorship."""
    # note: needs local font on server
    txt = "Jakub.Noniewicz.art.pl"
    fnt = ImageFont.truetype(font='./timesbi.ttf', size=14)
    twh = fnt.getsize(txt)
    bgx = (bg[0]^255&0xF0, bg[1]^255&0xF0, bg[2]^255&0xF0)
    bgx1 = (bgx[0]^0x80, bgx[1]^0x80, bgx[2]^0x80)
    x = w-twh[0]-2
    y = h-twh[1]-2
    draw.text((x+1, y+1), txt, font=fnt, fill=bgx1)
    draw.text((x, y), txt, font=fnt, fill=bgx)

def append_myself(title=""):
    """Append some tags to PNG image."""
    x = PngImagePlugin.PngInfo()
    today = dt.today()
    sdt = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    y = today.year
    x.add_text(key='Title', value=title, zip=False)
    x.add_text(key='Description', value='generated in PyArtForms @'+sdt, zip=False)
    x.add_text(key='Author', value='Jakub Noniewicz', zip=False)
    x.add_text(key='Copyright', value='(c)'+str(y)+' Jakub Noniewicz | noniewicz.com | noniewicz.art.pl', zip=False)
    x.add_itxt(key='Concept', value='PyArtForms concept by: Jakub Noniewicz | noniewicz.com | noniewicz.art.pl', lang='', tkey='', zip=False)
    return x

def im2cgi(im, format='PNG'):
    """Output image in CGI mode as bytes to stdout."""
    ct = ''
    if format == 'PNG':
        ct = 'image/png'
    if format == 'JPG':
        ct = 'image/jpg'
    if format == 'GIF':
        ct = 'image/gif'
    if ct == '':
        ct = 'image/png'
        format = 'PNG'
    imgByteArr = io.BytesIO()
    if format == 'PNG':
        im.save(imgByteArr, format=format, pnginfo=append_myself('PyArtForms '+params['name']))
    else:
        im.save(imgByteArr, format=format)
    data = imgByteArr.getvalue()
    sys.stdout.write("Content-Type: "+ct+"\n")
    sys.stdout.write("Content-Length: " + str(len(data)) + "\n") # todo: chk if proper
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write(data)
    sys.stdout.flush()

def art_painter(params, png_file='example.png', output_mode='save', bw=False):
    """Main/common 'painter' call."""
    if 'bw' in params:
        bw = params['bw']
    else:
        bw = False
    if output_mode == 'save':
        start_time = dt.now()
        print('drawing %s... %s - ' % (params['name'], png_file), end="", flush=True) # note same line next
    if bw:
        im = Image.new('L', (params['w'], params['h']), (0)) # todo: bg par?
    else:
        im = Image.new('RGB', (params['w'], params['h']), params['Background'])

    if "alpha" in params and not bw:
        if params['alpha'] == True:
            draw = ImageDraw.Draw(im, 'RGBA')
        else:
            draw = ImageDraw.Draw(im)
    else:
        draw = ImageDraw.Draw(im)

    params['im'] = im  # pass the Image object too
    f = params['call']
    f(draw, params)
    im = params['im'] # fix?
    if "blur" in params:
        if params['blur'] == True:
            im = xsmooth(params, im)

    if output_mode == 'save':
        #add_myself(draw, params['w'], params['h'], params['Background'])
        im.save(png_file, dpi=(300,300), pnginfo=append_myself('PyArtForms '+params['name']))
        show_benchmark(start_time)
        draw = None #?
        im = None #?
        params['im'] = None #?
        return
    if output_mode == 'cgi':
        add_myself(draw, params['w'], params['h'], params['Background'])
        im2cgi(im, format='PNG')
        return
    if output_mode == 'preview':
        return im

def get_cgi_par(default=None):
    """Parse CGI parameters"""
    form = cgi.FieldStorage()
    if default == None:
        par = {'w': 800, 'h': 600, 'f': '', 'n': 0}
    else:
        par = default
    if "w" in form:
        par['w'] = int(form["w"].value)
    if "h" in form:
        par['h'] = int(form["h"].value)
    if "f" in form:
        par['f'] = form["f"].value
    if "n" in form:
        par['n'] = int(form["n"].value)
    return par

def show_benchmark(start_time):
    """Show benchmark."""
    time_elapsed = dt.now() - start_time
    print('done. elapsed time: {}'.format(time_elapsed))
    return time_elapsed

def im2arr(image_path):
    """Image to array."""
    #im = Image.load(image_path)
    im = Image.open(image_path)
    im = im.convert('L')
    a = np.fromiter(iter(im.getdata()), np.uint8) # BW?
    a.resize(im.height, im.width)
    return a

def xsmooth(im):
    """Smooth image - 2x blur then sharpen back"""
    im = im.filter(ImageFilter.BLUR)
    im = im.filter(ImageFilter.BLUR)
    im = im.filter(ImageFilter.SHARPEN)
    im = im.filter(ImageFilter.SHARPEN)
    return im

def invert_image(image):
    """ Inverse image """
    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        rgb_image = Image.merge('RGB', (r, g, b))
        inverted_image = ImageOps.invert(rgb_image)
        r2, g2, b2 = inverted_image.split()
        return Image.merge('RGBA', (r2, g2, b2, a))
    else:
        return ImageOps.invert(image)
