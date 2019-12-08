import wx


class MyFrame (wx.Frame):
  def __init__(self,*args,**kwargs):
    super(MyFrame, self) .__init__(*args,**kwargs)
    self.InitUI()
  def InitUI(self):

    #创建菜单栏.
    self.menuBar = wx.MenuBar()

    #创建菜单，添加到菜单栏.
    self.menu_file = wx.Menu()
    self.menu_edit = wx. Menu ()
    self.menu_style = wx.Menu()
    self.menu_help =wx.Menu()
    self.menuBar.Append(self.menu_file, "文件")
    self.menuBar. Append(self.menu_edit, "编辑")
    self.menuBar.Append(self.menu_style,'格式')
    self.menuBar.Append(self.menu_help, '帮助')

    #创建菜单项，添加到指定菜单。
    self.Menuitem_new=self.menu_file.Append(wx.ID_NEW,"新建\tCtrl+N")
    self.Menuitem_open = self.menu_file.Append(wx.ID_OPEN, "打开\tCtrl+O")
    self.Menuitem_save = self.menu_file.Append(wx.ID_SAVE, "保存\tCtrl+S")
    self.Menuitem_exit = self.menu_file.Append(wx.ID_EXIT, "退出\tCtrl+E")

    #创建菜单项，添加到指定菜单。
    self.Menuitem_copy=self.menu_edit.Append(wx.ID_COPY,"复制Ctrl+E")
    self.Menuitem_cut = self.menu_edit.Append(wx.ID_OPEN, "剪切")
    self.Menuitem_paste = self.menu_edit.Append(wx.ID_SAVE, "粘贴")
    self.Menuitem_change = self.menu_style.Append(wx.DIRP_CHANGE_DIR, "修改格式")
    self.Menuitem_about = self.menu_help.Append(wx.ID_ABOUT, "关于")
    self.Menuitem_sysinf = self.menu_help.Append(wx.SYS_BORDER_X, "系统信息")

    #将菜单栏添加到窗体
    self.SetMenuBar(self.menuBar)

    #绑定事件
    self.Bind(wx.EVT_MENU, self.OnNew, self.Menuitem_new)
    self.Bind(wx.EVT_MENU, self.OnOpen, self.Menuitem_open)
    self.Bind(wx.EVT_MENU, self.OnSave, self.Menuitem_save)
    self.Bind(wx.EVT_MENU, self.OnQuit, self.Menuitem_exit)
    self.Bind(wx.EVT_MENU, self.OnCopy, self.Menuitem_copy)
    self.Bind(wx.EVT_MENU, self.OnCut, self.Menuitem_cut)
    self.Bind(wx.EVT_MENU, self.OnPaste, self.Menuitem_paste)
    self.Bind(wx.EVT_MENU, self.OnChange, self.Menuitem_change)
    self.Bind(wx.EVT_MENU, self.OnAbout, self.Menuitem_about)
    self.Bind(wx.EVT_MENU, self.OnSysinf, self.Menuitem_sysinf)

  # 设置窗体
    self.SetSize((400,300))
    self.SetTitle("记事本")
    panel=wx.Panel(self)
    #s = wx.StaticText(panel, label='欢迎来到python世界！', pos=(80, 40))
    self.Center()
    self.Show()
  # 菜单项事件处理方法.
  def OnNew(self, e):
    frame1=wx.Frame(parent=None,title='新建文件',size=(300,200),pos=(300,300))
    panel=wx.Panel(frame1)
    frame1.Show()

  def OnOpen(self, e):
    frame1 = wx.Frame(parent=None, title='打开文件', size=(300, 200), pos=(300, 300))
    panel = wx.Panel(frame1)
    frame1.Show()
  def OnSave(self, e):pass
  def OnQuit(self, e): self.Close()  # 退出程序 .
  def OnCopy(self, e):pass
  def OnCut(self, e):pass
  def OnPaste(self, e):pass
  def OnChange(self, e):
    dlg = wx.FontDialog(self,wx. FontData())
    if dlg.ShowModal()==wx.ID_OK:
      font = dlg.GetFontData().GetChosenFont()
      self.SetFont(font)
      dlg.Destroy()
  def OnAbout(self, e):pass
  def OnSysinf(self, e):pass

app = wx.App()
MyFrame(None)
app.MainLoop()
