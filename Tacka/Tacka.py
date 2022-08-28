import math

class Tacka:
    br_tacaka = 0        
    t_kreiranja = None   
#konstruktor koji se poziva pri kreiranju objekta
    def __init__(self, x = 0, y = 0):   
        self.x = x       
        self.y = y       
        Tacka.br_tacaka += 1
#ispisuje podatke o objektu   
    def predstavi_se(self):
        print("({:.2f}, {:f}".format(self.x, self.y))  
#ispisuje rastojanje izmedju dve odabrane tacke tako sto racuna rastojanje do druge tacke t 
    def rastojanje_do(self, t):  
        dx = self.x - t.x        
        dy = self.y - t.y
        return math.sqrt(dx**2 + dy**2)
#pretvara u string tj daje mogucnost print(t) ili str(t)
    def __str__(self):                                
        return "({:f}),{:f})".format(self.x, self.y) 
#proveri da li su dve tacke jednake  
    def __eq__(self, t):                               
        if isinstance(t,Tacka):                       
            return self.x == t.x and self.y == t.y
        return False
#sabira dva vektora definisana tackama
    def __add__(self, t):                               
        return Tacka(self.x + t.x, self.y + t.y)
#Ispisuje broj tacaka koje su napravljene do sada
    @staticmethod             
    def statistika():    
        p1 = "Broj kreiranih tacaka: "
        print(p1,Tacka.br_tacaka)
