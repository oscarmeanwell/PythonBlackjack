from tkinter import *
import random, sys
root = Tk()
UserBreaker = 0
MultiUserScore = 0
MultiCompScore = 0 
class Window():
    def __init__(self, parent):
        global UserBreaker
        self.labels = {}
        self.images = {}
        self.CompImages = {}
        self.CompLabels = {}
        self.parent = parent
        self.parent.title("21")
        self.parent.resizable(0,0)
        self.parent.grid()
        self.parent.geometry("800x800")
        self.parent.configure(background="dark green")
       
        self.Deck = ['club1','club2','club3','club4','club5','club6','club7','club8','club9','club10','club11','club12','club13', 'spade1','spade2','spade3','spade4','spade5','spade6','spade7','spade8','spade9','spade10','spade11','spade12','spade13', 'heart1','heart2','heart3','heart4','heart5','heart6','heart7','heart8','heart9','heart10','heart11','heart12','heart13', 'diamond1','diamond2','diamond3','diamond4','diamond5','diamond6','diamond7','diamond8','diamond9','diamond10','diamond11','diamond12','diamond13']
        self.SuitDeck = ['spade','club','heart','diamond']
        self.AddWindow()
        self.DealUser()
        self.AddButtons()
        self.BustBreaker = True 
        
    def AddWindow(self):
        self.FULL = Frame(self.parent, bg = "dark green")
        self.FULL.grid(row = 0, column = 0)
        self.TitleFrm = Frame(self.FULL, bg = "dark green")
        self.title = Label(self.TitleFrm, text = "Welcome To Pontoon you Loon!", bg="dark green", font=("Calibri", 26))
        self.title.grid(row = 0, column = 0, padx = 120)
        self.TitleFrm.grid(row = 0, column = 0)
        self.CardFrm = Frame(self.FULL, bg = "dark green")
        self.CardFrm.grid(row = 1, column = 0)
        self.BtnFrm = Frame(self.FULL, bg = "dark green")
        self.BtnFrm.grid(row = 3, column = 0)
        self.LblFrm = Frame(self.FULL, bg = "dark green")
        self.LblFrm.grid(row = 2, column = 0)
        self.CompCardFrm = Frame(self.FULL, bg = "dark green")
        self.CompCardFrm.grid(row = 4, column = 0)
        self.CompLblCardFrm = Frame(self.FULL, bg = "dark green")
        self.CompLblCardFrm.grid(row = 5, column = 0)
        self.CalcLblFrm = Frame(self.FULL, bg = "dark green")
        self.CalcLblFrm.grid(row = 6, column = 0)
        self.ScoresFrm = Frame(self.FULL, bg = "dark green")
        self.ScoresFrm.grid(row = 7, column = 0)
        self.EndBtnFrm = Frame(self.FULL, bg = "dark green")
        self.EndBtnFrm.grid(row = 8, column = 0)

    def DealUser(self):
        self.CardOneIndex = random.randint(0, 12)
        self.CardTwoIndex = random.randint(0, 12)
        self.CardOneSuitIndex = random.randint(0, 3)
        self.CardTwoSuitIndex = random.randint(0, 3) 
        self.CardOneConcatinated = self.SuitDeck[self.CardOneSuitIndex]+ str(self.CardOneIndex + 1)
        self.CardTwoConcatinated = self.SuitDeck[self.CardTwoSuitIndex]+ str(self.CardTwoIndex + 1)
        self.CardOnePos = self.Deck.index(self.CardOneConcatinated)
        self.CardTwoPos = self.Deck.index(self.CardTwoConcatinated)
        self.Deck[self.CardOnePos] = 'Gone'
        self.Deck[self.CardTwoPos] = 'Gone'
        self.CardOneGraphicFile = PhotoImage(file = 'images/'+self.CardOneConcatinated + '.gif')
        self.CardTwoGraphicFile = PhotoImage(file = 'images/'+self.CardTwoConcatinated + '.gif')
        self.CardOneGraphic = Label(self.CardFrm, image = self.CardOneGraphicFile)
        self.CardTwoGraphic = Label(self.CardFrm, image = self.CardTwoGraphicFile)
        self.CardOneGraphic.grid(row = 1, column = 0, padx = 20, pady = 20)
        self.CardTwoGraphic.grid(row = 1, column = 1, padx = 20, pady = 20)
        self.CardSum = 1
        self.CardOne = ''
        self.CardTwo = ''
        self.Txt = ''
        for Item in self.CardOneConcatinated:
            if Item in ['1','2','3','4','5','6','7','8','9', '0']:
                self.CardOne += Item

        for Item in self.CardTwoConcatinated:
            if Item in ['1','2','3','4','5','6','7','8','9', '0']:
                self.CardTwo += Item
        if int(self.CardOne) > 9:
            self.CardOne = '10'

        if int(self.CardTwo) > 9:
            self.CardTwo = '10'
        self.CardSum = int(self.CardOne) + int(self.CardTwo)
        self.SumLbl = Label(self.LblFrm, text = "The sum of your cards is: " + str(self.CardSum), bg = "dark green")
        self.SumLbl.grid(row = 2, column = 0)

    def AddButtons(self):
        self.Counter = 1
        self.TwistBtn = Button(self.BtnFrm, text = "Twist", height = 2, width = 5, fg = "blue", activebackground = "yellow", command = self.Twist)
        self.TwistBtn.grid(row = 3, column = 0, padx = 20, pady = 20)
        self.StickBtn = Button(self.BtnFrm, text = "Stick", height = 2, width = 5, fg = "blue", activebackground = "yellow", command = self.Stick)
        self.StickBtn.grid(row = 3, column = 1, padx = 20, pady = 20)

    def Stick(self):
        self.TxtStick = "The sum of your cards is: " + str(self.CardSum)
        self.SumLbl = Label(self.LblFrm, text = self.TxtStick, bg = "dark green")
        self.SumLbl.grid(row = 2, column = 0)
        self.PlayComputer()

    def Twist(self):
        global UserBreaker
        self.Breaker = True
        while self.Breaker:
            self.Cont = True
            self.CardNewIndex = random.randint(0, 12)
            self.CardNewSuitIndex = random.randint(0, 3)
            self.CardNewConcatinated = self.SuitDeck[self.CardNewSuitIndex]+ str(self.CardNewIndex + 1)
            self.CardNewPos = 0
            try:
                self.CardNewPos = self.Deck.index(self.CardNewConcatinated)
            except:
                self.Cont = False
            self.NewCard = ''
            if self.Deck[self.CardNewPos] != 'Gone' and self.Cont == True:
                self.Counter += 1
                self.hold = 'Lbl' + str(self.Counter)
                self.Deck[self.CardNewPos] = 'Gone'
                self.images[self.hold] = PhotoImage(file ='images/'+self.CardNewConcatinated + '.gif')
                self.labels[self.hold] = Label(self.CardFrm, image = self.images[self.hold])
                self.labels[self.hold].grid(row = 1, column = self.Counter, padx = 20, pady = 20)
                for Item in self.CardNewConcatinated:
                    if Item in ['1','2','3','4','5','6','7','8','9', '0']:
                        self.NewCard += Item

                if int(self.NewCard) > 9:
                    self.NewCard = 10
                self.CardSum += int(self.NewCard)
                self.Breaker = False
                
                if self.CardSum > 21:
                    self.Txt = "Busted! The sum of your cards is: " + str(self.CardSum)
                    UserBreaker = 1
                else:
                    self.Txt = "The sum of your cards is: " + str(self.CardSum)
                self.SumLbl = Label(self.LblFrm, text = self.Txt, bg = "dark green")
                self.SumLbl.grid(row = 2, column = 0)
            else:
                pass

        if UserBreaker != 0:
            self.PlayComputer()

    def PlayComputer(self):
        self.CompCardSum = 0
        self.Loop = -1
        while self.CompCardSum <= 17:
            self.CompLoop = True
            self.CompCardOneIndex = random.randint(0, 12)
            self.CompCardOneSuitIndex = random.randint(0, 3)
            self.CompCardOneConcatinated = self.SuitDeck[self.CompCardOneSuitIndex]+ str(self.CompCardOneIndex + 1)
            self.CompCardOnePos = 0
            try:
                self.CompCardOnePos = self.Deck.index(self.CompCardOneConcatinated)
            except:
                self.CompLoop = False

            if self.Deck[self.CompCardOnePos] != 'Gone' and self.CompLoop:
                self.Loop += 1
                self.Deck[self.CompCardOnePos] = 'Gone'
                self.Hold = "Lbl" + str(self.Loop)
                self.CompImages[self.Hold] = PhotoImage(file = 'images/'+self.CompCardOneConcatinated + '.gif')
                self.CompLabels[self.Hold] = Label(self.CompCardFrm, image = self.CompImages[self.Hold])
                self.CompLabels[self.Hold].grid(row = 0, column = self.Loop, padx = 20, pady = 20)
                self.CompCardOne = ''
                for Item in self.CompCardOneConcatinated:
                    if Item in ['1','2','3','4','5','6','7','8','9', '0']:
                        self.CompCardOne += Item

                if int(self.CompCardOne) > 9:
                    self.CompCardOne = '10'
                self.CompCardSum += int(self.CompCardOne)
                
            else:
                pass
        else:
            pass

        if self.CompCardSum > 21:
            self.Lbl2text = "The Computer was bust with a sum of: " + str(self.CompCardSum)

        else:
            self.Lbl2text = "The computer got: " + str(self.CompCardSum)

        self.SumLbl = Label(self.CompLblCardFrm, text = self.Lbl2text, bg = "dark green")
        self.SumLbl.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.CalcScores()

    def CalcScores(self):
        global MultiCompScore, MultiUserScore
        FinLblText = ''
        if (self.CardSum < 22 and self.CompCardSum < 22 and self.CardSum > self.CompCardSum) or (self.CardSum < 22 and self.CompCardSum > 21):
            FinLblText = "You Win!!"
            MultiUserScore += 1

        elif self.CompCardSum == self.CardSum or self.CardSum > 21 and self.CompCardSum > 21 :
            FinLblText = "Its a Draw!!"
            MultiUserScore += 1
            MultiCompScore += 1
            
        else:
            FinLblText = "The Computer Wins!!"
            MultiCompScore += 1

        self.CalcLbl = Label(self.CalcLblFrm, text = FinLblText, bg = "dark green")
        self.CalcLbl.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.UsrLbl = Label(self.ScoresFrm, text = ("User: " + str(MultiUserScore)), bg = "dark green" )
        self.CmpLbl = Label(self.ScoresFrm, text = ("Computer: " + str(MultiCompScore)), bg = "dark green" )
        self.UsrLbl.grid(row = 0, column = 0)
        self.CmpLbl.grid(row = 1, column = 0)
        self.AddEndBtn()

    def AddEndBtn(self):
        self.AgainBtn = Button(self.EndBtnFrm, text = "Again", height = 2, width = 5, fg = "blue", activebackground = "yellow", command = self.Again)
        self.AgainBtn.grid(row = 0, column = 0, padx = 20, pady = 20)
        self.QuitBtn = Button(self.EndBtnFrm, text = "Quit", height = 2, width = 5, fg = "blue", activebackground = "yellow", command = self.Quit)
        self.QuitBtn.grid(row = 0, column = 1, padx = 20, pady = 20)

    def Quit(self):
        self.parent.destroy()
        sys.exit()

    def Again(self):
        self.FULL.destroy()
        Window(root)
        root.mainloop()
        
        
        
if __name__ == '__main__':
    Window(root)
    root.mainloop()

        
       
        
