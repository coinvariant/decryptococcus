import wx, cv2
import numpy as np
from wx.core import OR_INVERT, VERTICAL

IMAGE = None
IMAGE_BUFFER = None


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
        global IMAGE, IMAGE_BUFFER

        img = cv2.imread(self.image_path[0])
        IMAGE = cv2.cvtColor(np.uint8(img), cv2.COLOR_BGR2RGB)
        IMAGE_BUFFER = IMAGE.copy() 


class PanelWithButtons(wx.Panel):
    def __init__(self, parent): 
        super().__init__(parent)

        vbox = wx.BoxSizer(orient=wx.VERTICAL)

        b1 = wx.Button(self, label = "Geometric filter")
        s1 = wx.Slider(self, style = wx.SL_AUTOTICKS)   
        b2 = wx.Button(self, label = "Erosion")
        b3 = wx.Button(self, label = "Dilation")
        b4 = wx.Button(self, label = "Averaging")
        b5 = wx.Button(self, label = "Gamma")
        b6 = wx.Button(self, label = "Logarithmic")

        vbox.Add(b1, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        vbox.Add(s1, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)    
        vbox.Add(b2, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)   
        vbox.Add(b3, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)   
        vbox.Add(b4, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        vbox.Add(b5, wx.ID_ANY, wx.EXPAND | wx.ALL, 20) 
        vbox.Add(b6, wx.ID_ANY, wx.EXPAND | wx.ALL, 20) 
             
        self.SetSizer(vbox)

        s1.SetTickFreq(5)
        print(s1.GetTickFreq())

        self.Bind(wx.EVT_BUTTON, self.OnGeometricPress, b1)
        self.Bind(wx.EVT_BUTTON, self.OnErosionPress, b2)
        self.Bind(wx.EVT_BUTTON, self.OnDilationPress, b3)
        self.Bind(wx.EVT_BUTTON, self.OnAveragePress, b4)
        self.Bind(wx.EVT_BUTTON, self.OnGammaPress, b5)
        self.Bind(wx.EVT_BUTTON, self.OnLogarithmicPress, b6)


        self.SetBackgroundColour((225, 225, 225))
    
    def OnErosionPress(self, e):
        print("Erosion")    
    
    def OnDilationPress(self, e):
        print("Dilation")

    def OnGeometricPress(self, e):
        print("Geometric")

    def OnAveragePress(self, e):
        print("Average")

    def OnGammaPress(self, e):
        print("Gamma")

    def OnLogarithmicPress(self, e):
        print("Logarithmic")

    


class PanelWithImage(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        wx.EVT_PAINT(self, self.on_paint)

        self.SetBackgroundColour((225, 225, 225))


    def on_paint(self, e):
        canvas = wx.PaintDC(self)
        h, w = IMAGE_BUFFER.shape[:2]
        bmp = wx.Bitmap.FromBuffer(w, h, IMAGE_BUFFER)
        canvas.DrawBitmap(bmp, 30, 20)



app = wx.App()
frame = AppFrame(None, "Decryptococcus")
frame.Show()
app.MainLoop()