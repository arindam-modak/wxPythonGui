import wx

class BasicApp(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(BasicApp,self).__init__(*args,**kwargs)
        self.make()

    def make(self):
        panel = wx.Panel(self)
        
        menubar = wx.MenuBar()

        menuButton1 = wx.Menu()
        editButton = wx.Menu()

        exitItem = menuButton1.Append(wx.ID_EXIT,'EXIT')

        menubar.Append(menuButton1,'File')
        menubar.Append(editButton,'Edit')
        
        
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.Quit,exitItem)

        username=""
        nameBox = wx.TextEntryDialog(None,'what is your name?','Welcome','name')
        if nameBox.ShowModal()==wx.ID_OK:
            username = nameBox.GetValue()

        yesnobox = wx.MessageDialog(None,'Are you Human ?','Questions',wx.YES_NO)
        yesnoanswer = yesnobox.ShowModal()
        yesnobox.Destroy()

        wx.TextCtrl(panel, pos=(15,10),size=(200,250))

        if yesnoanswer == wx.ID_NO:
            username = 'Loser!'
        
        self.SetTitle('Hello '+username)
        self.Show(True)

    def Quit(self,e):
        self.Close()
    
def main():
    app = wx.App();
    BasicApp(None)
    app.MainLoop()

main()
