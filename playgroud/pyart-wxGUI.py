#! /usr/bin/env python
# -*- coding: utf-8 -*-

# wx GUI for pyartforms
# (c)2019 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20190420
# upd: 20190421


# TODO:
# - remap paramsets to ctl and back / also get values
# - allow save (diff sizes)
# - render from memo txt
# - defs - add desc names + even longer desc
# - render - allow extra params to file names (from defs)
# - render - allow storage of all rnd par/val for EXACT rerender
# - ?


import wx
from PIL import Image, ImageDraw
from drawtools import *
from smears import *
from pyart_defs import *
from life1 import life
from lissajous import lissajous, lissajous_loop
from waves import *
from astroart import *
from mandelbrot import generate_mandelbrot



def PIL2wx(image):
    width, height = image.size
    return wx.Bitmap.FromBuffer(width, height, image.tobytes())



class GUIFrame(wx.Frame):
    """My window"""

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(GUIFrame, self).__init__(*args, **kw)

        # preview images size
        #self.w = 640
        #self.h = 480
        self.w = 800
        self.h = 600

        pnl = wx.Panel(self)
        self.pnl = pnl

        # and put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="pyartforms controls", pos=(10, 0))
        font = st.GetFont()
        font.PointSize += 2
        font = font.Bold()
        st.SetFont(font)

        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("pyartforms GUI")

        screenSize = wx.DisplaySize()
        mazy_all = ['mazy01', 'mazy02', 'mazy03', 'mazy04', 'mazy05', 'mazy06', 'mazy07', 'mazy08',
                    'mazy09', 'mazy10', 'mazy11', 'mazy12', 'mazy13', 'mazy14', 'mazy15', 'mazy16', 
                    'life', 'lissajous', 'waves', 'astro', 'mandelbrot',
                    ]
        x0 = 10 # ctl x0

        # smear selector
        self.cm = wx.ComboBox(pnl, id=wx.ID_ANY, value="", pos=(x0, 20), size=(70, 20), choices=mazy_all, style=0, validator=wx.DefaultValidator)
        self.cm.Bind(wx.EVT_COMBOBOX, self.OnSmearChanged)
        # preset selector
        self.sp = wx.SpinCtrl(pnl, id=wx.ID_ANY, value="0", pos=(x0, 20+30), size=(70, 20), style=wx.SP_ARROW_KEYS, min=0, max=1, initial=0)
        # go btn
        bn = wx.Button(pnl, id=wx.ID_ANY, label="GO", pos=(x0, 20+60), size=wx.DefaultSize, style=0, validator=wx.DefaultValidator)
        bn.Bind(wx.EVT_BUTTON, self.OnClicked) 

        #self.sl = wx.Slider(pnl, id=wx.ID_ANY, value=0, minValue=0, maxValue=100, pos=(x0, 20+90), size=wx.DefaultSize, style=wx.SL_HORIZONTAL, validator=wx.DefaultValidator)

        #self.cb = wx.CheckBox(pnl, id=wx.ID_ANY, label="chk", pos=(x0, 20+120), size=wx.DefaultSize, style=0, validator=wx.DefaultValidator)

        self.tx = wx.TextCtrl(pnl, id=wx.ID_ANY, value="", pos=(x0, 20+150), size=(400,300), style=wx.TE_MULTILINE, validator=wx.DefaultValidator)

        # preview image
        im = Image.new('RGB', (self.w, self.h), (0,0,0))
        bitmap = PIL2wx(im)
        self.bm = wx.StaticBitmap(pnl, id=wx.ID_ANY, bitmap=bitmap, pos=(screenSize[0]-self.w-20, 0), size=(self.w, self.h), style=0)
        

    def makeMenuBar(self):
        """Make menu bar with menus / menu items."""

        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        renderMenu = wx.Menu()

        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        renderItem = renderMenu.Append(-1, "&Go...\tF5", "Render image")

        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(renderMenu, "&Render")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        # associate handler function with the EVT_MENU event for each of the menu items
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnRender, renderItem)

    def do_mazy_p(self, w, h, x, name):
        if name in predefs:
            pr = predefs[name]
            p = pr(w, h)
        px = p[x]
        px['alpha'] = True #test
        self.tx.Value = str(px)
        im = art_painter(params=px, png_file='preview.png', output_mode='preview', bw=False)
        return im

    def OnClicked(self, event): 
        btn = event.GetEventObject().GetLabel() 
        #print("DEBUG: Label of pressed button = ", btn)
        if btn == 'GO':
            self.doRender()

    def OnSmearChanged(self, event):
        mn = self.cm.Value
        pr = predefs[mn]
        cnt = len(pr(0, 0))
        self.sp.SetMax(cnt-1)
        self.sp.SetValue(0)
        #print("DEBUG: OnSmearChanged:", mn, 'cnt:', cnt)

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("Hello again")

    def OnRender(self, event):
        self.doRender()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("pyartforms GUI v1.0beta", "About", wx.OK|wx.ICON_INFORMATION)

    def doRender(self): 
            mn = self.cm.Value
            n = self.sp.Value
            im = self.do_mazy_p(self.w, self.h, n, mn)
            self.bm.SetBitmap(PIL2wx(im))


if __name__ == '__main__':
    # When this module is run (not imported) then create app/frame, show it, and start the event loop.
    app = wx.App()
    screenSize = wx.DisplaySize()
    frm = GUIFrame(None, id=wx.ID_ANY, title='pyartforms GUI', pos=(0,0), size=screenSize, style=wx.DEFAULT_FRAME_STYLE, name='gui')
    frm.Show()
    app.MainLoop()


