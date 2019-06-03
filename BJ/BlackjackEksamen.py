import random


typer = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
numre = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
værdier = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

igangværendeSpil = True

class Kort:
    
    def __init__(self,farve,nummer):
        self.farve = farve
        self.nummer = nummer
        
    def __str__(self):
        return self.nummer + ' : ' + self.farve
    

class Spil:
    
    def __init__(self):
        self.spil = []  # empty list
        for farve in typer:
            for nummer in numre:
                self.spil.append(Kort(farve, nummer))
                
    def __str__(self):
        spil_komp = ''  # start with an empty string
        for kort in self.spil:
            spil_komp += '\n '+kort.__str__() 
        return 'spil_komp:' + spil_komp
                
    def shuffle(self):
        random.shuffle(self.spil)
        
    def deal(self):
        enkeltKort = self.spil.pop()
        return enkeltKort
    

class Hånd:
    
    def __init__(self):
        self.kort2 = []  
        self.værdi = 0   
        self.ace = 0   
    
    def tilføjKort(self, kort):
        self.kort2.append(kort)
        self.værdi += værdier[kort.nummer]
        if kort.nummer == 'ace':
            self.ace += 1  # add to self.aces
    
    def justerAce(self):
        while self.værdi > 21 and self.ace:
            self.værdi -= 10
            self.ace -= 1
            

class Penge:
    
    def __init__(self):
        self.total = 100
        self.indsæt = 0
        
    def vinderBet(self):
        self.total += self.indsæt
    
    def taberBet(self):
        self.total -= self.indsæt
        



def FormBet(tokens):

    while True:
        try:
            tokens.indsæt = int(input('Hvor mange tokens vil du indsætte? '))
        except ValueError:
            print('Ikke vær silly, det skal være en integer!')
        else:
            if tokens.indsæt > tokens.total:
                print("Sorry, du kan ikke overstige ding pung",tokens.total)
            else:
                break

def slå(spil,hånd):
    hånd.tilføjKort(spil.deal())
    hånd.justerAce()
    
def slåEllerStands(spil,hånd):
    
    global igangværendeSpil
    
    while True:
        i = input("Vil du slå eller standse: 'h' for slå 's' for standse")
        
        if i[0].lower() == 'h':
            slå(spil,hånd) 

        elif i[0].lower() == 's':
            print("Spiller standser. Dealers tur")
            
            igangværendeSpil = False

        else:
            print("Kun 'h' eller 's' ")
            continue
        break

    
def VisInfo(spiller,dealer):
    print("\nDealer's Hånd:")
    print(" !! Skjult hånd !!")
    print('',dealer.kort2[1])  
    print("\nSpillers Hånd:", *spiller.kort2, sep='\n ')
    
def visAlt(spiller,dealer):
    print("\nDealer's Hånd:", *dealer.kort2, sep='\n ')
    print("Dealer's Hånd =",dealer.værdi)
    print("\nPlayer's Hand:", *spiller.kort2, sep='\n ')
    print("Player's Hånd =",spiller.værdi)
    
def spillerTaber(spiller,dealer,tokens):
    print("Spiller taber!")
    tokens.taberBet()    

def spillerVinder(spiller,dealer,tokens):
    print("Spiller vinder!")
    tokens.vinderBet()

def dealerTaber(spiller,dealer,tokens):
    print("Dealer taber!")
    tokens.vinderBet()
    
def dealerVinder(spiller,dealer,tokens):
    print("Dealer vinder!")
    tokens.taberBet()
    
def uafgjort(spiller,dealer):
    print("Uafgjort.")
    


while True:
    print("<=============================================>")
    print("Velkommen til denne blackjack spil! reglerne er simple")
    print("Slå så tæt på til 21, ellers taber du\nDealer slår til og aces vil blive talt som 1 eller 11.")
    print("<=============================================>")
    
    spil = Spil()
    spil.shuffle()
    
    spilleHånd = Hånd()
    spilleHånd.tilføjKort(spil.deal())
    spilleHånd.tilføjKort(spil.deal())
    
    dealerHånd = Hånd()
    dealerHånd.tilføjKort(spil.deal())
    dealerHånd.tilføjKort(spil.deal())
    

    SpillerPenge = Penge()  
    
 
    FormBet(SpillerPenge)
    
   
    VisInfo(spilleHånd,dealerHånd)
    
    while igangværendeSpil:  
        
       
        slåEllerStands(spil,spilleHånd)
        VisInfo(spilleHånd,dealerHånd)
        
        if spilleHånd.værdi > 21:
            spillerTaber(spilleHånd,dealerHånd,SpillerPenge)
            break
    

    if spilleHånd.værdi <= 21: 
        while dealerHånd.værdi < 17:
            slå(spil,dealerHånd)
            
        
        visAlt(spilleHånd,dealerHånd)
        
        
        if dealerHånd.værdi > 21:
            dealerTaber(spilleHånd,dealerHånd,SpillerPenge)

        elif dealerHånd.værdi > spilleHånd.værdi:
            dealerVinder(spilleHånd,dealerHånd,SpillerPenge)

        elif dealerHånd.værdi < spilleHånd.værdi:
            spillerVinder(spilleHånd,dealerHånd,SpillerPenge)

        else:
            uafgjort(spilleHånd,dealerHånd)

      
    print("\nSpillers pose ligger på: ",SpillerPenge.total)
    
   
    nytSpil = input("Vil du gerne spille igen? Tryk 'j' eller alt andet! ")
    if nytSpil[0].lower()=='j':
        igangværendeSpil=True
        continue
    else:
        print("Thanks for playing!")
        break
