from array import *

class sms():

    def __init__(self, modelname):
        if modelname.find("T1tttt") != -1: self.T1tttt()
        #if modelname.find("T6bbsleptonMET150") != -1: self.T6bbsleptonMET150()
        #if modelname.find("T6bbslepton") != -1: self.T6bbslepton()
        if modelname == "T6bbsleptonMET150": self.T6bbsleptonMET150()
        if modelname == "T6bbslepton": self.T6bbslepton()
        if modelname.find("T5ttttDM175") != -1: self.T5ttttDM175()
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T1qqqq") != -1: self.T1qqqq()
        if modelname.find("TChiWZ") != -1: self.TChiWZ()
        if modelname.find("TSlepton") != -1: self.TSlepton()
        if modelname.find("TSlepton_noPURW") != -1: self.TSlepton_noPURW()
        if modelname.find("TSleptonLeft") != -1: self.TSleptonLeft()
        if modelname.find("TSleptonRight") != -1: self.TSleptonRight()


    def T6bbslepton(self):
        # model name
        self.modelname = "T6bbslepton"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{b} #tilde{b}, #tilde{b} #rightarrow b #tilde{#chi}^{0}_{2}, #tilde{#chi}^{0}_{2} #rightarrow #tilde{l} l, #tilde{l} #rightarrow l #tilde{#chi}^{0}_{1}"
        self.label2= "#tilde{#chi}^{0}_{1} = 100 GeV";
        # scan range to plot
        self.Xmin = 400.
        self.Xmax = 1500.
        self.Ymin = 150.
        self.Ymax = 1450.
        self.Zmin = 0.001
        self.Zmax = 0.01
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{b}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{#tilde{#chi}^{0}_{2}}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.diagX = array('d',[400,600,900])
        self.diagY = array('d',[212.5,412.5,712.5])

    def TChiWZ(self):
        # model name
        self.modelname = "TChiWZ"
        # decay chain
        #lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{#chi}^{#pm}_{1}#tilde{#chi}^{0}_{2}; #tilde{#chi}^{2}_{0} #rightarrow Z + #tilde{#chi}^{1}_{0}, #tilde{#chi}^{#pm}_{1} #rightarrow W^{#pm} + #tilde{#chi}^{0}_{1}"
        self.label2= ""
        # scan range to plot
        self.Xmin = 100.
        self.Xmax = 700.
        self.Ymin = 0.
        self.Ymax = 300.
        self.Zmin = 0.01
        self.Zmax = 0.5
        # produce sparticle
        self.sParticle = "m(#tilde{#chi}_{2}^{0}) = m(#tilde{#chi}_{1}^{#pm}) [GeV]"
        # LSP
        self.LSP = "m(#tilde{#chi}^{0}_{1}) [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        self.diagX = array('d',[400,600,900])
        self.diagY = array('d',[212.5,412.5,712.5])



    def T6bbsleptonMET150(self):
        # model name
        self.modelname = "T6bbsleptonMET150"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{b} #tilde{b}, #tilde{b} #rightarrow b #tilde{#chi}^{0}_{2}, #tilde{#chi}^{0}_{2} #rightarrow #tilde{l} l, #tilde{l} #rightarrow l #tilde{#chi}^{0}_{1}"
        self.label2= "#tilde{#chi}^{0}_{1} = 100 GeV";
        # scan range to plot
        self.Xmin = 400.
        self.Xmax = 900.
        self.Ymin = 200.
        self.Ymax = 900.
        self.Zmin = 0.05
        self.Zmax = 0.3
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{b}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{#tilde{#chi}^{0}_{2}}} [GeV]"
        # turn off diagonal lines
        self.diagOn = True
        self.diagX = array('d',[400,600,900])
        self.diagY = array('d',[212.5,412.5,712.5])

    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} "+lsp_s;
        self.label2= "";
        # scan range to plot
        self.Xmin = 700.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        
    def T5ttttDM175(self):
        # model name
        self.modelname = "T5ttttDM175"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g},  #tilde{g} #rightarrow #tilde{t}_{1} t,  #tilde{t}_{1} #rightarrow #bar{t} "+lsp_s;
        self.label2= "m_{#tilde{t}_{1}} - m_{#tilde{#chi}^{0}_{1}} = 175 GeV";
        # scan range to plot
        self.Xmin = 600.
        self.Xmax = 1700.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} "+lsp_s;
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1800.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False                                                                                                                

    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
        self.label2= "";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600.
        self.Xmax = 1950.
        self.Ymin = 0.
        self.Ymax = 1600.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{g}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False

    def TSlepton(self):
        # model name
        self.modelname = "TSlepton"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{e}_{L/R} #tilde{e}_{L/R}, #tilde{#mu}_{L/R} #tilde{#mu}_{L/R}";
        self.label2= "BR( #tilde{l} #rightarrow  l "+lsp_s +" ) = 1";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 75.
        self.Xmax = 1000.
        self.Ymin = 1.
        self.Ymax = 800.
        self.Zmin = 1e-5
        self.Zmax = 1
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{l}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False                                                                                                                

    def TSlepton_noPURW(self):                                                                                                      
        # model name
        self.modelname = "TSlepton_noPURW"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{e}_{L/R} #tilde{e}_{L/R}, #tilde{#mu}_{L/R} #tilde{#mu}_{L/R}";
        self.label2= "BR( #tilde{l} #rightarrow  l "+lsp_s +" ) = 1";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 50.
        self.Xmax = 600.
        self.Ymin = 1.
        self.Ymax = 450.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{l}}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False                                                                                               


    def TSleptonLeft(self):
        # model name
        self.modelname = "TSleptonLeft"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{e}_{L} #tilde{e}_{L}, #tilde{#mu}_{L} #tilde{#mu}_{L}";
        self.label2= "BR( #tilde{l} #rightarrow  l "+lsp_s +" ) = 1";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 75.
        self.Xmax = 600.
        self.Ymin = 10.
        self.Ymax = 450.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{l} (Left handed)}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False                                                                                                

    def TSleptonRight(self):
        # model name
        self.modelname = "TSleptonRight"
        # decay chain
        lsp_s = "#lower[-0.12]{#tilde{#chi}}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}"
        self.label= "pp #rightarrow #tilde{e}_{R} #tilde{e}_{R}, #tilde{#mu}_{R} #tilde{#mu}_{R}";
        self.label2= "BR( #tilde{l} #rightarrow  l "+lsp_s +" ) = 1";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 75.
        self.Xmax = 450.
        self.Ymin = 10.
        self.Ymax = 350.
        self.Zmin = 0.001
        self.Zmax = 2.
        # produce sparticle
        self.sParticle = "m#kern[0.1]{_{#lower[-0.12]{#tilde{l} (Right handed)}}} [GeV]"
        # LSP
        self.LSP = "m#kern[0.1]{_{"+lsp_s+"}} [GeV]"
        # turn off diagonal lines
        self.diagOn = False                                                                                                
    
