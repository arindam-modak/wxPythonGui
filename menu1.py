import wx

class BasicApp(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(BasicApp,self).__init__(*args,**kwargs)
        self.make()

    def make(self):
        menubar = wx.MenuBar()
        menuButton1 = wx.Menu()
        exitItem = menuButton1.Append(wx.ID_EXIT,'EXIT')
        menubar.Append(menuButton1,'File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.Quit,exitItem)
        self.SetTitle('Hello World')
        self.Show(True)

    def Quit(self,e):
        self.Close()
    
def main():
    app = wx.App();
    BasicApp(None)
    app.MainLoop()

main()
