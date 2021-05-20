import wx

class TestFrame(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size = (1400,900))

        self.initialize_GUI()
    
    def initialize_GUI(self):
        self.sp = wx.SplitterWindow(self, style = wx.SP_3DBORDER)
        self.p1 = PanelWithButtons(self.sp)
        self.p2 = wx.Panel(self.sp)
        self.sp.SplitVertically(self.p1, self.p2, 300)


        self.p2.SetBackgroundColour((225, 225, 225))

        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        filequit = filemenu.Append(wx.ID_EXIT, "Quit", "Quit application")
        fileopen = filemenu.Append(wx.ID_FILE, "Open", "Open an image")

        menubar.Append(filemenu, "&File")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, filequit)
        # self.Bind(wx.EVT_MENU. load_file, fileopen)

        self.SetTitle("Menu")
        self.Centre()


    def OnQuit(self, e):
        self.Close()

    def load_file(self, e):
        pass
        

class PanelWithButtons(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        button = wx.Button(self, label = "Help me")

        self.SetBackgroundColour((225, 225, 225))



app = wx.App()
frame = TestFrame(None, "Decryptococcus")
frame.Show()
app.MainLoop()