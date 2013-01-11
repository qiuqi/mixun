#! /usr/bin/env python
#coding=utf-8
import wx
import os

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,300))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() #A Statusbar in the bottom of the window

        #Setting up the menu
        filemenu = wx.Menu()

        #wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, u"打开(&O)", u"打开文件")
        menuAbout = filemenu.Append(wx.ID_ABOUT, u"关于(&A)", u"关于密讯")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, u"离开(&X)", u"离开")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0,6):
            self.buttons.append(wx.Button(self, -1, u"按钮&"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
            
        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"文件(&F)")
        self.SetMenuBar(menuBar)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show(True)
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, u"密讯保证你的通讯安全", u"关于密讯", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self, e):
        self.Close(True)
        
    def OnOpen(self, e):
        """ Open a file """
        self.dirname = ''
        dlg = wx.FileDialog(self, u"选择一个文件", self.dirname,"","*.*",wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None,u"密讯")
app.MainLoop()
