import wx
from wx.core import LIGHT_GREY, Size

class equacaoFrame(wx.Frame):

    def __init__(self, parent, title):
        super(equacaoFrame, self).__init__(parent, title=title)
    
        self.locale = wx.Locale(wx.LANGUAGE_PORTUGUESE_BRAZILIAN)
        #criando uma barra de menu#
        self.makeMenuBar()

        #criando uma barra de status#
        self.CreateStatusBar()
        self.SetStatusText("Trabalho realizado pelos alunos do IC UFAL")

        #criando entrada
        self.InitEntrada()
        #Mudando o Icone
        self.InitIcone()



    #Mudando o icone da tela  
    def InitIcone(self):    
        self.icon =wx.Icon(wx.Bitmap("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/alpha.png"))#path to icon
        self.SetIcon(self.icon)
        self.Show()

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        saveItem = fileMenu.Append(-1, "&Salvar\tCtrl+S",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        saveitemas = fileMenu.Append(-1, "&Salvar como\tCtrl+Shift+S",
                "Salvar como")        
        
        fileMenu.AppendSeparator()
        openitem = fileMenu.Append(wx.ID_OPEN)
        
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        


        helpmenu = wx.Menu()
        aboutItem = helpmenu.Append(wx.ID_ABOUT)


        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&Arquivo")
        menuBar.Append(helpmenu, "&Ajuda")
        
        self.SetMenuBar(menuBar)

        
        self.Bind(wx.EVT_MENU, self.Onsave, saveItem)
        self.Bind(wx.EVT_MENU, self.Onsaveas, saveitemas)
        self.Bind(wx.EVT_MENU, self.Onexit,  exitItem)
        self.Bind(wx.EVT_MENU, self.Onsobre, aboutItem)
        self.Bind(wx.EVT_MENU, self.Onopen, openitem)

    #ações do Menu 
    def Onsave(self, event):
       wx.MessageBox("salvar aquivo")

    def Onsaveas(self, event):
     with wx.FileDialog(self,"Save as XYZ file", wildcard="xyz files (*.xyz)|*.xyz",
                        style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT) as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return   
        pathname = fileDialog.GetPath()
        try:
            with open(pathname, 'w') as file:
                self.doSaveData(file)
        except IOError:
            wx.LogError("Cannot save current data in file '%s'." % pathname)
   
    def Onexit(self, event):
        self.Close(True)
    def Onsobre(self, event):       
        wx.MessageBox("Trabalho feito por alunos do IC UFAL")
    def Onopen(self, event):
        wx.FileSelector("Escolha um arquivo")

    def InitEntrada(self):

        Tela = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)

        text = wx.StaticText(Tela, label="Digite sua equação abaixo:")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        tc = wx.TextCtrl(Tela)
        sizer.Add(tc, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        Tela.SetSizer(sizer)
        #inserindo botao de enviar e limpar 
        buttonsend = wx.Button(Tela, label="Enviar", size=(90, 28))
        buttonClear = wx.Button(Tela, label="Limpar", size=(90, 28))
        sizer.Add(buttonsend, pos=(2, 2))
        sizer.Add(buttonClear, pos=(2, 3), flag=wx.RIGHT|wx.Right, border=10)

        #Inserindo botões de imagem
        beta = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/beta.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.betabutton = wx.BitmapButton(Tela, -1, beta, pos=(5,100), size =(beta.GetWidth()+5, beta.GetHeight()+5))

        alpha = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/alpha.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.alphabutton = wx.BitmapButton(Tela, -1, alpha, pos=(60,100), size =(alpha.GetWidth()+5, alpha.GetHeight()+5))

        theta = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/theta.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.thetabutton = wx.BitmapButton(Tela, -1, theta, pos=(115,100), size =(theta.GetWidth()+5, theta.GetHeight()+5))

        delta = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/delta.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.deltabutton = wx.BitmapButton(Tela, -1, delta, pos=(170,100), size =(delta.GetWidth()+5, delta.GetHeight()+5))

        omega = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/omega.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.omegabutton = wx.BitmapButton(Tela, -1, omega, pos=(225,100), size =(omega.GetWidth()+5, omega.GetHeight()+5))

        sigma = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/sigma.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.sigmabutton = wx.BitmapButton(Tela, -1, sigma, pos=(280,100), size =(sigma.GetWidth()+5, sigma.GetHeight()+5))

        
        menorq = wx.Image("C:/Users/Paloma lacerda/Documents/estruturas/Ab2/Icones/lessthan.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.menorqbutton = wx.BitmapButton(Tela, -1, menorq, pos=(335,100), size =(menorq.GetWidth()+5, menorq.GetHeight()+5))








        #definindo cor de background
        Tela.SetBackgroundColour(LIGHT_GREY)

        #criando linha de separação
        line = wx.StaticLine(Tela)
        sizer.Add(line, pos=(3,0), span=(1,5), 
                flag = wx.EXPAND|wx.BOTTOM, border = 10)

        #pra a entrada se encaixar na tela
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)



   
       


def main():

    app = wx.App()
    ex = equacaoFrame(None, title='Editor de equação')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
