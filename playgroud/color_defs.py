#! /usr/bin/env python
# -*- coding: utf-8 -*-

# experimental paint algorithms (artificial artist) in Python, v1.0
# (c)2017-2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz

# color definitions


# white yellow red lb1 lb2 blue ltgray gray
colors_happy = [(255,255,255), (0xEC, 0xD1, 0x27), (0xD1, 0x3B, 0x29), (0x7F, 0xAE, 0xAD),
                (0x41, 0x8D, 0xB0), (0x29, 0x56, 0x80), (0xB0, 0xB0, 0xB0), (0x90, 0x90, 0x90)]

colors_happy_nw7 = [(0xEC, 0xD1, 0x27), (0xD1, 0x3B, 0x29), (0x7F, 0xAE, 0xAD),
                (0x41, 0x8D, 0xB0), (0x29, 0x56, 0x80), (0xB0, 0xB0, 0xB0), (0x90, 0x90, 0x90)]

# white yellow red blue x2
colors_fwd = [(255,255,255), (0xEC, 0xD1, 0x27), (0xD1, 0x3B, 0x29), (0x20, 0x50, 0xA0),
              (255,255,255), (0xEC, 0xD1, 0x27), (0xD1, 0x3B, 0x29), (0x20, 0x50, 0xA0)]

colors_fwd_nw6 = [(0xEC, 0xD1, 0x27), (0xD1, 0x3B, 0x29), (0x20, 0x50, 0xA0),
              (0xEC, 0xD1, 0x27), (0xD1, 0x3B, 0x29), (0x20, 0x50, 0xA0)]

# bw x2
colors_bw = [(0xff, 0xff, 0xff), (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff), (0xc0, 0xc0, 0xc0),
          (0xff, 0xff, 0xff), (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff), (0xc0, 0xc0, 0xc0),
          ]

# pastel psychedelic
colors_p = [(0x78, 0xE6, 0x7B),
          (0x8F, 0x60, 0xEE),
          (0xFE, 0x7B, 0x65),
          (0xE7, 0x5F, 0xE5),
          (0x7B, 0xA4, 0xE0),
          (0xFF, 0x9C, 0x6B),
          (0xEB, 0xDD, 0x67),
          (0xFA, 0x60, 0x93),
          ]

# magic blue with little green (better for print?)
colors_b = [(0x00, 0x10, 0x20),
          (0x00, 0x20, 0x40),
          (0x00, 0x30, 0x60),
          (0x00, 0x40, 0x80),
          (0x00, 0x50, 0xA0),
          (0x00, 0x60, 0xC0),
          (0x00, 0x70, 0xE0),
          (0x00, 0x80, 0xFF),
          ]

# just yellow
colors_y = [(0x20, 0x20, 0x00),
          (0x40, 0x40, 0x00),
          (0x60, 0x60, 0x00),
          (0x80, 0x80, 0x00),
          (0xA0, 0xA0, 0x00),
          (0xC0, 0xC0, 0x00),
          (0xE0, 0xE0, 0x00),
          (0xFF, 0xFF, 0x00),
          ]

# ---

def old_colorer(params):
    r = 0
    g = 0
    b = 0
    if 'r1' in params and 'r0' in params: 
        if params['r1'] > 0:
            r = random.randint(params['r0'], params['r1'])
    if 'g1' in params and 'g0' in params: 
        if params['g1'] > 0:
            g = random.randint(params['g0'], params['g1'])
    if 'b1' in params and 'b0' in params: 
        if params['b1'] > 0:
            b = random.randint(params['b0'], params['b1'])
    return (r, g, b)

#def new_colorer(mode):
#    return 0

def add_alpha(color, alpha):
    return (color[0], color[1], color[2], alpha)
