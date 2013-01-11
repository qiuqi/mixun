#! /usr/bin/env python
#coding=utf-8
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() #A Statusbar in the bottom of the window

        #Setting up the menu
        filemenu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, u"关于(&A)", u"关于密讯")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, u"离开(&X)", u"离开")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"文件(&F)")
        self.SetMenuBar(menuBar)
        self.Show(True)
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, u"密讯保证你的通讯安全", u"关于密讯", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self, e):
        self.Close(True)

app = wx.App(False)
frame = MainWindow(None,u"密讯")
app.MainLoop()
