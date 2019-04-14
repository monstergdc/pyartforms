#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 20190328, 29
# 20190401, 02, 14

# this one needs also ?

# IDEA
#smears - napisy long
#color-fade
#size-fade
#stackup
#opt linear fade (optyk)
# by spiral from center big->smal | small->bog
# spec chr for enter
# wariant rnd ale mniejsze pozniej
# tez w gwiazde left=center

import random, math, string, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
from drawtools import *
from color_defs import *


#Commodore 64 Pixelized
#Commodore 64 Rounded
#CooperBlack-WP EE
#Coronet
#Diager
#Dirty Dung Solid
#Dirty Dung
#Earth People
#Elementarz
#EnglishTowne-Normal
#EngrvrsOldEng Bd BT
#Eppy Evans Round Light
#FiveFingerDiscount
#Franklin Gothic Heavy
#Freefrm721 Blk L2
#Georgia Pogrubiona kursywa
#Georgia Pogrubiony

f = [
    'VITAMIN.TTF',
    'TRANSIST.TTF',
    'SLANT.TTF',
    'PAC-FONT.TTF',
    'MaszynaAEG.ttf',
    'MAILBOMB.TTF',
    'tahoma.ttf', # Tahoma (PL)
    'zxspectr.ttf',
    'zxspectr1.ttf',
    'WESTWOOD.TTF',
    'TAHALM P.TTF',
    'STHLMGRA.TTF', # Sthlm graffiti
    'SKINCK_.TTF', # SkinnyCapKick
    'SHOPLIFT.TTF', # Shoplifters unite
    'SCRIBAN.TTF', # Scriba LET
    'RUBSTAMP.TTF', # Rubber Stamp LET
    'PLASTICB.TTF', # Plastic Bag
    'PLANETBE.TTF', # Planet Benson
    'PABLON.TTF', # Pablo LET
    'simsun.ttc', # NSimSun - for chinese
    'ONE8SEVE.TTF', # one8seven
    'NECK CAN.TTF', # Neck Candy
    'nasaliza.ttf', # Nasalization
    'LOKICOLA.TTF', # Loki Cola
    'KUBA_REC.TTF', # Kuba_reczny (PL)
    'Kobajashi.ttf', # Kobajashi
    'KILLATV.TTF', # Kailler Ants Trial Version
    'impact.ttf', # Impact
    ]

sentence1 = \
    "Litwo, Ojczyzno moja! ty jesteś jak zdrowie; \
    Ile cię trzeba cenić, ten tylko się dowie, \
    Kto cię stracił. Dziś piękność twą w całej ozdobie \
    Widzę i opisuję, bo tęsknię po tobie. \
    Panno święta, co Jasnej bronisz Częstochowy \
    I w Ostrej świecisz Bramie! Ty, co gród zamkowy \
    Nowogródzki ochraniasz z jego wiernym ludem! \
    Jak mnie dziecko do zdrowia powróciłaś cudem \
    (— Gdy od płaczącej matki, pod Twoją opiekę \
    Ofiarowany martwą podniosłem powiekę; \
    I zaraz mogłem pieszo, do Twych świątyń progu \
    Iść za wrócone życie podziękować Bogu —) \
    Tak nas powrócisz cudem na Ojczyzny łono!... \
    Tymczasem, przenoś moją duszę utęsknioną \
    Do tych pagórków leśnych, do tych łąk zielonych, \
    Szeroko nad błękitnym Niemnem rozciągnionych; \
    Do tych pól malowanych zbożem rozmaitem, \
    Wyzłacanych pszenicą, posrebrzanych żytem; \
    Gdzie bursztynowy świerzop, gryka jak śnieg biała, \
    Gdzie panieńskim rumieńcem dzięcielina pała, \
    A wszystko przepasane jakby wstęgą, miedzą \
    Zieloną, na niej zrzadka ciche grusze siedzą."

sentence2 = \
 "Okrponości świata |\
 | \
 Spowiły nas trujące opary |\
 Tam uciekają ludziska... |\
 Z życiem się dzisiaj weźmiesz za bary |\
 Spadasz z wielkiego urwiska. |\
 | \
 Bombowce biorą nasze namiary |\
 Najgłośniej piszczy hipiska |\
 Brak uczuć, chęci, czasem brak wiary |\
 Najwięcej czart tu uzyska! |\
 | \
 To nietoperze, węże, kalmary |\
 Już hen w oddali gdzieś błyska... |\
 Bystro śmigają nawet niezdary |\
 Tam szatan czarta wyiska... |\
 | \
 Życie odkrywa swoje przywary |\
 Czart rozpala paleniska |\
 Niegroźne przy nich nawet Atari |\
 Złowroga brzmią ich nazwiska."



def txt_rnd(draw, params):
    w = params['w']
    h = params['h']
    cnt = params['cnt']
    txt = params['txt']
    mode = params['mode']
    cmode = params['cmode']
    f = params['font']
    random.seed()
    z0 = 640+360
    zn = z0
    for i in range(cnt):
        x = random.randint(int(-w*0.4), int(w*0.7))
        y = random.randint(int(-h*0.3), h)
        n = random.randint(0, 7)
        if cmode == 0:
            c = (colors_happy[n][0], colors_happy[n][1], colors_happy[n][2])
        else:
            if cmode == 1:
                c = (colors_p[n][0], colors_p[n][1], colors_p[n][2])
            else:
                c0 = int(255-255*i/cnt)
                c = (c0, c0, c0)
        if mode == 0:
            z = random.randint(36, 640)
        else:
            z = zn + random.randint(0, 20)
            zn = zn - int(z0/cnt*0.9)
        fnt = ImageFont.truetype(font=f, size=z)
        draw.text((x, y), txt, font=fnt, fill=c)

def txt_down(params):
    w = params['w']
    h = params['h']
    cnt = params['cnt']
    txt = params['txt']
    cmode = params['cmode']
    size = params['size']
    dsize = params['dsize']
    random.seed()
    d = ImageDraw.Draw(img)
    y = 0 # init
    # dy dsize - wylicz proper
    for i in range(cnt):
        fnt = ImageFont.truetype(f, size)
        twh = fnt.getsize(txt)
        x = int((w-twh[0])/2)
        if cmode == 0:
            n = random.randint(0, 7)
            c = (colors_happy[n][0], colors_happy[n][1], colors_happy[n][2])
        else:
            n = i%7
            c = (colors_happy[n][0], colors_happy[n][1], colors_happy[n][2])
        d.text((x, y), txt, font=fnt, fill=c)
        y += int(twh[1]*0.9) # note overflow
        size -= dsize

def txt_go(draw, params):
    w = params['w']
    h = params['h']
    a = params['a']
    cmode = params['cmode']
    sizemin = params['sizemin']
    sizemax = params['sizemax']
    cspace = params['cspace']
    rspace = params['rspace']
    f = params['font']
    x0 = params['x0']
    random.seed()
    y = 0 # init
    x = 0 # init
    twh_old = (0, 0)
    for i in range(len(a)):
        txt = a[i]
        size = random.randint(sizemin, sizemax)
        fnt = ImageFont.truetype(f, size)
        twh = fnt.getsize(txt)
        if txt == '|':  #simulated enter
            x = x0
            y += int(sizemax * cspace)
        else:
            if x + twh[0] > w:
                x = x0
                y += int(twh_old[1] * rspace)
            c = (0, 0, 0)
            if cmode == 1:
                n = random.randint(0, 6)
                c = (colors_happy_nw7[n][0], colors_happy_nw7[n][1], colors_happy_nw7[n][2])
            if cmode == 2:
                n = random.randint(0, 5)
                c = (colors_fwd_nw6[n][0], colors_fwd_nw6[n][1], colors_fwd_nw6[n][2])
            draw.text((x, y), txt, font=fnt, fill=c)
            x += twh[0] + 1
        twh_old = twh

# wtf cos nie dziala
def txt_circle(params):
    w = params['w']
    h = params['h']
    txt = params['txt']
    #cmode = params['cmode']
    #d_out = ImageDraw.Draw(img)
    for i in range(36):
        ti = Image.new('RGBA', (w, h), color = (255, 255, 255))
        d = ImageDraw.Draw(ti)
        size = 128
        fnt = ImageFont.truetype(f, size)
        n = random.randint(0, 6)
        c = (colors_happy_nw7[n][0], colors_happy_nw7[n][1], colors_happy_nw7[n][2])
        d.text((int(w/2), int(h/2)), txt, font=fnt, fill=c)
        wi = ti.rotate(i*10, expand=1) # par
        #img.paste(wi, box=None, mask=None)
        img_out = Image.blend(img, wi)
        img = img_out

# --- go


#w, h = get_canvas('1024')
#w, h = get_canvas('A4')
w, h = get_canvas('A3')
#w, h = get_canvas('A2')
#w, h = get_canvas('A1')

start_time = dt.now()
root = '!output-txt'
if not os.path.exists(root):
    os.makedirs(root)
odir = root+'\\'

txt_M = "MONSTER"
txt_m = "monster"
txt_Mo = "MoNsTeR"
txt_gdc = "GDC"
txt_grych = "GRYCH"
txt_non = "Noniewicz.art.pl"
txt_cn = '屁股' # dupa in CN, use NSimSun font
txt_kon = "KONSTYTUCJA"

a1 = sentence1.split()
a2 = sentence2.split()

cnt = 1

p = [
    {'name': 'txt-non-mailbomb', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_non, 'font': 'MAILBOMB.TTF', 'cnt': 240, 'mode': 1, 'cmode': 0},
    {'name': 'txt-non-mailbomb', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_non, 'font': 'MAILBOMB.TTF', 'cnt': 200, 'mode': 1, 'cmode': 1},
    {'name': 'txt-non-mailbomb', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_non, 'font': 'MAILBOMB.TTF', 'cnt': 200, 'mode': 1, 'cmode': -1},
    {'name': 'txt-non-mailbomb', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_non, 'font': 'MAILBOMB.TTF', 'cnt': 18, 'mode': 1, 'cmode': -1, 'size': 600, 'dsize': 32},
    {'name': 'txt-non-f4', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_non, 'font': f[4], 'cnt': 18, 'mode': 1, 'cmode': -1, 'size': 600, 'dsize': 32},
    {'name': 'txt-konst-mailbomb', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_kon, 'font': 'MAILBOMB.TTF', 'cnt': 240, 'mode': 1, 'cmode': 0},
    {'name': 'txt-konst-RUBSTAMP', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_kon, 'font': 'RUBSTAMP.TTF', 'cnt': 240, 'mode': 1, 'cmode': 0},
    {'name': 'txt-konst-KUBA_REC', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_kon, 'font': 'KUBA_REC.TTF', 'cnt': 240, 'mode': 1, 'cmode': 0},
    {'name': 'txt-konst-Kobajashi', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_kon, 'font': 'Kobajashi.ttf', 'cnt': 240, 'mode': 1, 'cmode': 0},
    {'name': 'txt-konst-MaszynaAEG', 'call': txt_rnd, 'w': w, 'h': h, 'Background': (255,255,255), 'txt': txt_kon, 'font': 'MaszynaAEG.ttf', 'cnt': 240, 'mode': 1, 'cmode': 0},
    ]

for n in range(cnt):
    tx = dt.now().strftime('%Y%m%d%H%M%S')
    for i in range(len(p)):
        art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (p[i]['name'], w, h, i+1, n+1, tx))

p = [
    {'name': 'litwo-KUBA_REC', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a1, 'cmode': 1, 'sizemin': 300, 'sizemax': 700, 'font': 'KUBA_REC.TTF', 'cspace': 0.3, 'rspace': 0.35, 'x0': 150},
    {'name': 'litwo-Kobajashi', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a1, 'cmode': 1, 'sizemin': 112, 'sizemax': 360, 'font': 'Kobajashi.ttf', 'cspace': 0.5, 'rspace': 0.9, 'x0': 15},
    {'name': 'litwo-SHOPLIFT', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a1, 'cmode': 1, 'sizemin': 112, 'sizemax': 360, 'font': 'SHOPLIFT.TTF', 'cspace': 0.5, 'rspace': 0.9, 'x0': 15},
    
    {'name': 'wieszcz1-KUBA_REC', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a2, 'cmode': 1, 'sizemin': 300, 'sizemax': 700, 'font': 'KUBA_REC.TTF', 'cspace': 0.3, 'rspace': 0.35, 'x0': 150},
    {'name': 'wieszcz1-Kobajashi', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a2, 'cmode': 1, 'sizemin': 112, 'sizemax': 360, 'font': 'Kobajashi.ttf', 'cspace': 0.5, 'rspace': 0.9, 'x0': 15},
    {'name': 'wieszcz1-tahoma', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a2, 'cmode': 1, 'sizemin': 112, 'sizemax': 360, 'font': 'tahoma.ttf', 'cspace': 0.5, 'rspace': 0.9, 'x0': 15},
    {'name': 'wieszcz1-MaszynaAEG', 'call': txt_go, 'w': w, 'h': h, 'Background': (255,255,255), 'a': a2, 'cmode': 1, 'sizemin': 112, 'sizemax': 360, 'font': 'MaszynaAEG.ttf', 'cspace': 0.5, 'rspace': 0.9, 'x0': 15},
    ]

for n in range(cnt):
    tx = dt.now().strftime('%Y%m%d%H%M%S')
    for i in range(len(p)):
        art_painter(p[i], odir+'%s-%dx%d-%02d-%03d-%s.png' % (p[i]['name'], w, h, i+1, n+1, tx))

time_elapsed = dt.now() - start_time
print('ALL done. elapsed time: {}'.format(time_elapsed))

