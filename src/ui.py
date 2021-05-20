import wx, cv2
import numpy as np

image_data = None
image_path = None

class TestFrame(wx.Frame):


    def __init__(self, parent, title):
        super().__init__(parent, title=title, size = (1400,900))

        image_data = None
        image_path = None

        self.initialize_GUI()
    
    def initialize_GUI(self):
        self.sp = wx.SplitterWindow(self, style = wx.SP_3DBORDER)
        self.p1 = PanelWithButtons(self.sp)
        self.p2 = PanelWithImage(self.sp)
        self.sp.SplitVertically(self.p1, self.p2, 300)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        filequit = filemenu.Append(wx.ID_EXIT, "Quit", "Quit application")
        fileopen = filemenu.Append(wx.ID_FILE, "Open", "Open an image")

        menubar.Append(filemenu, "&File")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, filequit)
        self.Bind(wx.EVT_MENU, self.OnBrowse, fileopen)

        self.Centre()


    def OnQuit(self, e):
        self.Close()

    def OnBrowse(self, e):
        with wx.FileDialog(None, "Choose a file", style=wx.ID_OPEN) as dialog:

            if dialog.ShowModal() == wx.ID_OK:
                self.image_path = dialog.GetPaths()
                self.load_file()

    def load_file(self):
        print(self.image_path)
        img = cv2.imread(self.image_path[0])
        img = cv2.cvtColor(np.uint8(img), cv2.COLOR_BGR2RGB) 

        h, w = img.shape[:2]

        wxbmp = wx.Bitmap.FromBuffer(w, h, img)
        self.p2.bmp = wxbmp
        

class PanelWithButtons(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        button = wx.Button(self, label = "Help me")

        self.SetBackgroundColour((225, 225, 225))

class PanelWithImage(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour((225, 225, 225))


app = wx.App()
frame = TestFrame(None, "Decryptococcus")
frame.Show()
app.MainLoop()