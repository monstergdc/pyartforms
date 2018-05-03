
# (c)2018 Noniewicz.com
# upd: 20180503

CANVASES = {
    'A4': (3507, 2480),
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
    '4000' : (4000, 3000),
    '8000' : (8000, 6000)
}

def get_canvas(name):
    return CANVASES.get(name, (0,0))

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
