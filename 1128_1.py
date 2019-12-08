import wx

class MyFrame(wx.Frame):
  pass

class MyFrame(wx.Frame):
  def __init__(self,*args,**kw):
    super(MyFrame,self).__init__(*args,**kw)
    self.InitUI()

  def InitUI(self):
    #创建菜单栏.
    self.menuBar = wx.MenuBar()

    # 创建菜单，添加到菜单栏
    self.menu_file = wx.Menu()
    self.menu_edit = wx.Menu()
    self.menu_format = wx.Menu()
    self.menu_about = wx.Menu()
    self.menuBar.Append(self.menu_file, "文件")
    self.menuBar.Append(self.menu_edit, "编辑")
    self.menuBar.Append(self.menu_format, "格式")
    self.menuBar.Append(self.menu_help, "帮助")
    # 创建菜单项，添加到指定菜单.
    self.Menuitem_new = self.menu_file.Append(wx.ID_NEW, "新建\tCtrl+N")
    self.Menuitem_open = self.menu_file.Append(wx.ID_OPEN, "打开\tCtrl+O")
    self.Menuitem_save = self.menu_file.Append(wx.ID_SAVE, "保存\tCtrl+S")
    self.Menuitem_exit = self.menu_file.Append(wx.ID_EXIT, "退出\tCtrl+E")
    self.Menuitem_copy = self.menu_edit.Append(wx.ID_COPY, "复制\tCtrl+C")
    self.Menuitem_cut = self.menu_edit.Append(wx.ID_CUT, "剪切\tCtrl+V")
    self.Menuitem_paste = self.menu_edit.Append(wx.ID_PASTE, "粘贴\tCtrl+X")
    self.Menuitem_font = self.menu_format.Append(wx.ID_FONT, "修改字体\tF")
    self.Menuitem_about = self.menu_help.Append(wx.ID_ABOUT, "关于\tA")
    self.Menuitem_message = self.menu_help.Append(wx.ID_MESSAGE, "系统信息\tH")

    #将菜单栏添加到窗体.
    self.SetMenuBar(self.menuBar)

    #绑定事件.
    self.Bind(wx.EVT_MENU,self.OnNew,self.Menuitem_new)
    self.Bind(wx.EVT_MENU,self.OnOpen,self.Menuitem_open)
    self.Bind(wx.EVT_MENU,self.OnSave,self.Menuitem_save)
    self.Bind(wx.EVT_MENU,self.OnQuit,self.Menuitem_exit)
    self.Bind(wx.EVT_MENU, self.OnCopy,self.Menuitem_copy)
    self.Bind(wx.EVT_MENU, self.OnCut, self.Menuitem_cut)
    self.Bind(wx.EVT_MENU, self.OnPaste, self.Menuitem_paste)
    self.Bind(wx.EVT_MENU, self.OnFont, self.Menuitem_font)
    self.Bind(wx.EVT_MENU, self.OnAbout, self.Menuitem_about)
    self.Bind(wx.EVT_MENU, self.OnHelp, self.Menuitem_help)

    # 设置窗体.
    self.SetSize((400, 300))
    self.SetTitle("记事本")
    self.Center()
    self.Show()

    # 菜单项事件处理方法.
    def OnNew(self, e):
      frame1 = wx.Frame(parent=None, title='新建文件', size=(300, 200), pos=(300, 300))
      panel = wx.Panel(frame1)
      frame1.Show()

    def OnOpen(self, e):
      frame1 = wx.Frame(parent=None, title='打开文件', size=(300, 200), pos=(300, 300))
      panel = wx.Panel(frame1)
      frame1.Show()

    def OnSave(self, e): pass

    def OnQuit(self, e): self.Close()  # 退出程序 .

    def OnCopy(self, e): pass

    def OnCut(self, e): pass

    def OnPaste(self, e): pass

    def OnChange(self, e):
      dlg = wx.FontDialog(self, wx.FontData())
      if dlg.ShowModal() == wx.ID_OK:
        font = dlg.GetFontData().GetChosenFont()
        self.SetFont(font)
        dlg.Destroy()

    def OnAbout(self, e): pass

    def OnSysinf(self, e): pass

  #if __name__ == '__main__':
    app = wx.App()
    MyFrame(None)
    app.MainLoop()
