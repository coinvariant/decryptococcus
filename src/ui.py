import wx, cv2
import numpy as np
from wx.core import VERTICAL


class AppFrame(wx.Frame):


    def __init__(self, parent, title):
        super().__init__(parent, title=title, size = (1400,900))

        self.initialize_GUI()
    

    def initialize_GUI(self):
        self.sp = wx.SplitterWindow(self, style = wx.SP_3DBORDER)
        self.p1 = PanelWithButtons(self.sp)
        self.p2 = PanelWithImage(self.sp)
        self.sp.SplitVertically(self.p1, self.p2, 300)


        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        fileopen = filemenu.Append(wx.ID_OPEN, "Open", "Open an image")
        filequit = filemenu.Append(wx.ID_EXIT, "Quit", "Quit application")

        menubar.Append(filemenu, "&File")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnBrowse, fileopen)
        self.Bind(wx.EVT_MENU, self.OnQuit, filequit)


        self.Centre()


    def OnQuit(self, e):
        self.Close()

    def OnBrowse(self, e):
        with wx.FileDialog(None, "Choose a file", style=wx.ID_OPEN) as dialog:

            if dialog.ShowModal() == wx.ID_OK:
                self.image_path = dialog.GetPaths()
                self.load_file()

    def load_file(self):
        img = cv2.imread(self.image_path[0])
        img = cv2.cvtColor(np.uint8(img), cv2.COLOR_BGR2RGB) 

        h, w = img.shape[:2]

        self.p2.bitmap = wx.Bitmap.FromBuffer(w, h, img)


class PanelWithButtons(wx.Panel):
    def __init__(self, parent): 
        super().__init__(parent)

        vbox = wx.BoxSizer(orient=wx.VERTICAL)
        b1 = wx.Button(self, label = "Geometric filter")
        b2 = wx.Button(self, label = "Erosion")
        b3 = wx.Button(self, label = "Dilation")
        b4 = wx.Button(self, label = "Averaging")

        vbox.Add(b1, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)  
        vbox.Add(b2, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)   
        vbox.Add(b3, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)   
        vbox.Add(b4, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)         


        self.SetSizer(vbox)

        self.SetBackgroundColour((225, 225, 225))


class PanelWithImage(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        self.bitmap = None

        wx.EVT_PAINT(self, self.on_paint)

        self.SetBackgroundColour((225, 225, 225))


    def on_paint(self, e):
        canvas = wx.PaintDC(self)
        canvas.DrawBitmap(self.bitmap, 30, 20)



app = wx.App()
frame = AppFrame(None, "Decryptococcus")
frame.Show()
app.MainLoop()