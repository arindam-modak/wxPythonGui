import wx

class BasicApp(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(BasicApp,self).__init__(*args,**kwargs)
        self.Show()

def main():
    app = wx.App();
    BasicApp(None)
    app.MainLoop()

main()
