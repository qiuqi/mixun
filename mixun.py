#! /usr/bin/env python
#coding=utf-8
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() #A Statusbar in the bottom of the window
        
        #Setting up the menu
        filemenu = wx.Menu()
        
        #wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Mixun IM")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit"

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()
