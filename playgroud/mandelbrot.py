# Mandelbrot fractal example (z'=z^2+c), v1.0, Python
# (c)2017, 2018 Noniewicz.com, Jakub Noniewicz aka MoNsTeR/GDC
# cre: 20180505

from PIL import Image, ImageDraw
import math
from datetime import datetime as dt

def generate_mandelbrot(x0, x1, y0, y1, maxiter, w, h, negative, png):
    start_time = dt.now()
    print('generating mandel...', w, h, 'iter', maxiter)
    im = Image.new('L', (w, h), (0))
    draw = ImageDraw.Draw(im)
    xs0 = abs(x1-x0)/w
    ys0 = abs(y1-y0)/h
    for y in range(h):
        for x in range(w):
            z = complex(0, 0)
            c = complex(x0+xs0*x, y0+ys0*y)
            i = 0
            noesc = True
            while (noesc == True) and (i < maxiter):
                z = z * z + c
                m = math.sqrt(z.real*z.real + z.imag*z.imag)
                if m >= 2:
                    ii = i
                    noesc = False
                i += 1
            if noesc == True:
                ii = maxiter
            pv = 1.0 - float(ii) / float(maxiter)
            if negative == True:
                pix = 255-round(pv*255)
            else:
                pix = round(pv*255)
            draw.point((x, y), fill=pix)
    time_elapsed = dt.now() - start_time
    print('done. elapsed time: {}'.format(time_elapsed))
    im.save(png, dpi=(300,300))

if __name__ == '__main__':
    generate_mandelbrot(-2.5, 1.0, -1.0, 1.0, 200, 700, 400, False, 'mandel-001.png')
    generate_mandelbrot(-2.5, 1.0, -1.0, 1.0, 20, 700, 400, False, 'mandel-002.png')

