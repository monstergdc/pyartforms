#! /usr/bin/env python
# -*- coding: utf-8 -*-

# wx GUI for PyArtForms
# (c)2019-2021 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# cre: 20190420
# upd: 20190421, 22, 26
# upd: 20210612, 13


# TODO:
# - remap paramsets to ctl and back / also get values
# - allow save (diff sizes)
# - defs - add desc names + even longer desc
# - render - allow extra params to file names (from defs)


import wx
import ast
import copy
from PIL import Image, ImageDraw
from drawtools import *
from pyart_defs import *



def PIL2wx(image):
    """Convert image from PIL to wx.Bitmap"""
    width, height = image.size
    return wx.Bitmap.FromBuffer(width, height, image.tobytes())



class GUIFrame(wx.Frame):
    """My window"""

    def __init__(self, *args, **kw):
        super(GUIFrame, self).__init__(*args, **kw)

        self.app = "PyArtForms"

        # preview images size
        self.w = 800
        self.h = 600

        pnl = wx.Panel(self)
        self.pnl = pnl

        st = wx.StaticText(pnl, label=self.app+" controls", pos=(10, 0))
        font = st.GetFont()
        font.PointSize += 2
        font = font.Bold()
        st.SetFont(font)

        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText(self.app+" GUI")

        screenSize = wx.DisplaySize()
        mazy_all = predef_names
        x0 = 10 # ctl x0
        y0 = 24 # ctl y0

        # smear selector
        self.st_v = wx.StaticText(pnl, label="Effect", pos=(x0, y0))
        self.cm = wx.ComboBox(pnl, id=wx.ID_ANY, value="", pos=(x0+70, y0), size=(120, 20), choices=mazy_all, style=0, validator=wx.DefaultValidator)
        self.cm.Bind(wx.EVT_COMBOBOX, self.OnSmearChanged)
        # preset selector
        self.st_v = wx.StaticText(pnl, label="Variant 0-?", pos=(x0, y0+30))
        self.sp = wx.SpinCtrl(pnl, id=wx.ID_ANY, value="0", pos=(x0+70, y0+30), size=(70, 20), style=wx.SP_ARROW_KEYS, min=0, max=1, initial=0)
        # go btns
        bn = wx.Button(pnl, id=wx.ID_ANY, label="Render", pos=(x0, y0+60), size=wx.DefaultSize, style=0, validator=wx.DefaultValidator)
        bn.Bind(wx.EVT_BUTTON, self.OnClicked) 
        bn2 = wx.Button(pnl, id=wx.ID_ANY, label="Render from text", pos=(x0+100, y0+60), size=wx.DefaultSize, style=0, validator=wx.DefaultValidator)
        bn2.Bind(wx.EVT_BUTTON, self.OnClicked) 
        # params preview
        self.tx = wx.TextCtrl(pnl, id=wx.ID_ANY, value="", pos=(x0, y0+150), size=(400,400), style=wx.TE_MULTILINE, validator=wx.DefaultValidator)

        #self.sl = wx.Slider(pnl, id=wx.ID_ANY, value=0, minValue=0, maxValue=100, pos=(x0, y0+90), size=wx.DefaultSize, style=wx.SL_HORIZONTAL, validator=wx.DefaultValidator)
        #self.cb = wx.CheckBox(pnl, id=wx.ID_ANY, label="chk", pos=(x0, y0+120), size=wx.DefaultSize, style=0, validator=wx.DefaultValidator)

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

        exitItem = fileMenu.Append(wx.ID_EXIT)
        renderItem = renderMenu.Append(-1, "&Render...\tF5", "Render image")
        render2Item = renderMenu.Append(-1, "&Render from text...\tF6", "Render image from text")
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(renderMenu, "&Render")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnRender, renderItem)
        self.Bind(wx.EVT_MENU, self.OnRender2, render2Item)

    def do_mazy_p(self, w, h, n, name):
        if name in predefs:
            pr = predefs[name]
            p = pr(w, h)
        px = p[n]
        px['alpha'] = True #test
        px_ = copy.deepcopy(px)
        px_['call'] = None
        self.tx.Value = str(px_)
        im = art_painter(params=px, png_file='preview.png', output_mode='preview', bw=False)
        return im

    def do_mazy_p2(self, w, h, n, name):
        px = ast.literal_eval(self.tx.Value)
        px['alpha'] = True #test
        pr = predefs[name]
        p = pr(w, h)
        px['call'] = p[0]['call']
        im = art_painter(params=px, png_file='preview.png', output_mode='preview', bw=False)
        return im

    def OnClicked(self, event):
        """Button clicks"""
        btn = event.GetEventObject().GetLabel() 
        #print("DEBUG: Label of pressed button = ", btn)
        if btn == 'Render':
            self.doRender()
        if btn == 'Render from text':
            self.doRender2()

    def OnSmearChanged(self, event):
        mn = self.cm.Value
        #print("DEBUG: OnSmearChanged:", mn)
        pr = predefs[mn]
        cnt = len(pr(0, 0))
        self.sp.SetMax(cnt-1)
        self.sp.SetValue(0)
        self.st_v.SetLabel("Variant 0-"+str(cnt-1))

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("Hello again") # todo: sth usefull

    def OnRender(self, event):
        self.doRender()

    def OnRender2(self, event):
        self.doRender2()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox(self.app+" GUI v1.0beta", "About", wx.OK|wx.ICON_INFORMATION)

    def doRender(self):
        """Main render call"""
        mn = self.cm.Value
        n = self.sp.Value
        im = self.do_mazy_p(self.w, self.h, n, mn)
        self.bm.SetBitmap(PIL2wx(im))

    def doRender2(self):
        """Main render call v2"""
        mn = self.cm.Value
        n = self.sp.Value
        im = self.do_mazy_p2(self.w, self.h, n, mn)
        self.bm.SetBitmap(PIL2wx(im))


if __name__ == '__main__':
    # when module is run (not imported)
    app = wx.App()
    screenSize = wx.DisplaySize()
    frm = GUIFrame(None, id=wx.ID_ANY, title='PyArtForms GUI', pos=(0,0), size=screenSize, style=wx.DEFAULT_FRAME_STYLE, name='pyagui')
    frm.Show()
    app.MainLoop()

